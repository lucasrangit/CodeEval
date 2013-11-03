#!/usr/bin/python
# https://www.codeeval.com/browse/116/
# Each letter is separated by space char, each word is separated by 2 space 
# chars.
# Morse code is in Internation (ITU) format.

# On CodeEval, test cases are read in from a file which is the first argument 
# to your program. Open the file and read in line by line. Each line 
# represents a different test case (unless given different instructions in the
# challenge description).

from sys import argv, stdout

#alpha2morse = {
#'A': '.-',
#'B': '-...',
#'C': '-.-.',
#'D': '-..',
#'E': '.',
#'F': '..-.',
#'G': '--.',
#'H': '....',
#'I': '..',
#'J': '.---',
#'K': '-.-',
#'L': '.-..',
#'M': '--',
#'N': '-.',
#'O': '---',
#'P': '.--.',
#'Q': '--.-',
#'R': '.-.',
#'S': '...',
#'T': '-',
#'U': '..-',
#'V': '...-',
#'W': '.--',
#'X': '-..-',
#'Y': '-.--',
#'Z': '--..',
#'1': '.----',
#'2': '..---',
#'3': '...--',
#'4': '....-',
#'5': '.....',
#'6': '-....',
#'7': '--...',
#'8': '---..',
#'9': '----.',
#'0': '-----',
#}

morse2alpha = {
'.-': 'A',
'-.-.': 'C',
'-...': 'B',
'.': 'E',
'-..': 'D',
'--.': 'G',
'..-.': 'F',
'..': 'I',
'....': 'H',
'-.-': 'K',
'.---': 'J',
'--': 'M',
'.-..': 'L',
'---': 'O',
'-.': 'N',
'--.-': 'Q',
'.--.': 'P',
'...': 'S',
'.-.': 'R',
'-': 'T',
'..-': 'U',
'.--': 'W',
'...-': 'V',
'-.--': 'Y',
'-..-': 'X',
'--..': 'Z',
'.----': '1',
'-----': '0',
'...--': '3',
'..---': '2',
'.....': '5',
'....-': '4',
'--...': '7',
'-....': '6',
'----.': '9',
'---..': '8',
}

# One-time build morse-to-alph dict.
# TODO input option to change case of alpha
# TODO sort by alpha (not required but more legible)
#print "#### CUT ####"
#print "morse2alpha = {"
#for alpha in alpha2morse:
#	print "'%s': '%s'," % (alpha2morse[alpha], alpha)
#print "}"
#print "#### CUT ####"

test_cases = open(argv[1], 'r')
 
for test in test_cases:
	# remove endline
	test = test.rstrip('\n')
    # ignore test if it is an empty line
	if (test == ''):
		continue
	# convert morse code 
	for morse in test.split(' '):
		if (morse == ''):
			stdout.write(' ') 
		else:
			stdout.write(morse2alpha[morse])
	print
 
test_cases.close()
