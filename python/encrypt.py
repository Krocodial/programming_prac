#!/usr/bin/python3.5

#investigate chr() and ord()
#built in functions used to see the unicode of a string

import sys
import os

if(len(sys.argv) < 3):
	print('not enough arguments')
	sys.exit()
try:
	inf = open(sys.argv[1], 'r')
except:
	print('error opening file')
	sys.exit()

print(os.path.splitext(sys.argv[1])[0] + '.jpg')

if(sys.argv[2] == 'encrypt'):
	outf = open(os.path.splitext(sys.argv[1])[0] + '.encr', 'w')
	for line in inf:
		line = line.rstrip()
		words = line.split()

		for w in words:
			outf.write(chr(
	


