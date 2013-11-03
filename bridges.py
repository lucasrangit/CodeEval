#!/usr/bin/python
# Bay Area Brige Challenge
# https://www.codeeval.com/open_challenges/109/
# 
# Author: Lucas Magasweran <lucas.magasweran@ieee.org>
#
# Segment intersection code from:
# http://www.bryceboe.com/2006/10/23/line-segment-intersection-algorithm/ 

# On CodeEval, test cases are read in from a file which is the first argument to your program
# Open the file and read in line by line. Each line represents a different test case
# (unless given different instructions in the challenge description)
 
import sys
from re import sub 
from itertools import combinations

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y 
	def __str__(self):
		return "[%r, %r]" % (self.x, self.y)

class Bridge:
	def __init__(self,i,a,b):
		self.i = i
		self.a = a
		self.b = b
	def __str__(self):
		return "%d: (%s, %s)" % (self.i, self.a, self.b)

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

test_cases = open(sys.argv[1], 'r')

bridges = list()

for test in test_cases:
    # 'test' represents the test case, do something with it

	# ignore test if it is an empty line
	if test.strip() == '':
		continue
	
	br, rest = test.split(':')
	points = list()
	for pt in rest.split(','):
		points.append(float(sub("[^0-9.-]", "", pt)))
	a = Point(points[0], points[1])
	b = Point(points[2], points[3])	
	br = Bridge(int(br), a, b)
	bridges.append(br)

def print_bridges(bridges):
	for bridge in bridges:
		print bridge

def print_bridge_numbers(bridges):
	"""Print sorted list of bridges, one per line"""
	numbers = list()
	for bridge in bridges:
		numbers.append(bridge.i)
	numbers.sort()
	for n in numbers:
		print n

test_cases.close()

def bridge_intersect_count(br1, bridges):
	"""Checks if an input bridge overlaps a list of bridges"""
	count = 0
	for br2 in bridges:
		if br1.i == br2.i:
			continue
		if intersect(br1.a, br1.b, br2.a, br2.b):
			count += 1
	return count

safe = list()
rejected = list()

# move bridge with zero intersections to safe list
# reject bridge with most intersections left in bridge list
while len(bridges) > 0:
	max_intersections = 0
	max_bridge = {}
	
	for bridge in bridges:
		count = bridge_intersect_count(bridge, bridges)
		if count == 0:
			safe.append(bridge)
		elif count >= max_intersections:
			max_intersections = count
			max_bridge = bridge

	if max_bridge:
		bridges.remove(max_bridge)
		rejected.append(max_bridge)

	# have to move those in safe list *after* iterating through
	# bridges so as not to modify list while iterating
	for bridge in safe:
		if bridge in bridges:
			bridges.remove(bridge)

#print "Safe:"
#print_bridges(safe)
#print "Unsafe"
#print_bridges(rejected)

print_bridge_numbers(safe)
