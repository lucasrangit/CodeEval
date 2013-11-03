#!/usr/bin/python
# CodeEval Open Challenge #114 - Knapsack
# 

import sys 
#from itertools import combinations

def combinations(iterable, r):
	# from http://docs.python.org/2/library/itertools.html
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

# return the total weight and value of list of packages
def packages_sum(packages):
	weight_sum = 0
	value_sum = 0
	for package in range(0, len(packages)):
		weight_sum += packages[package][1]
		value_sum += packages[package][2]
	return weight_sum, value_sum


test_cases = open(sys.argv[1], 'r')

# each line defines the capacity and the available packages
for test in test_cases:
	# skip blank lines
	if test.strip() == '':
		continue

	# packages Nx3 matrix
	# # | Weight | Value
	packages = []
	packages_max = []
	package_weight_max = 0
	package_cost_max = 0
	package_count_max = 0

	capacity, packages_string = test.split(" : ")
	capacity = float(capacity)
	for package in packages_string.split(" "):
		i, w, v = package.strip('(').strip(')').strip(')\n').split(',')
		packages.append([int(i), float(w), float(v.strip('$'))]) 
	
	# find the combination of package that
	# maximizes weight and value 
	# while total weight does not exceed capacity
	for count in range(1, len(packages)):
		for package in combinations(packages, count):
			package_weight, package_cost = packages_sum(package)
			if (package_weight > capacity):
				continue
			elif (package_cost > package_cost_max):
				package_cost_max = package_cost
				package_weight_max = package_weight
				package_count_max = count
				packages_max = list(package)
			elif (package_cost == package_cost_max and package_weight < package_weight_max):
				package_cost_max = package_cost
				package_weight_max = package_weight
				package_count_max = count
				packages_max = list(package)

	# none found
	if len(packages_max) == 0:
		print "-"
	
	# output packages in the format #,#,#,...
	elif len(packages_max) > 1:
		for package in range(0, len(packages_max)-1):
			print "%d," % (packages_max[package][0]),
			# don't insert space between concatenation
			sys.stdout.softspace=0
		print packages_max[-1][0]

	else:
		print packages_max[0][0]

test_cases.close()
