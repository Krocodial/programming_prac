#!/usr/bin/python3

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

#print(os.path.splitext(sys.argv[1])[0] + '.jpg')

if(sys.argv[2] == 'encrypt'):
	outf = open(os.path.splitext(sys.argv[1])[0] + '.encr', 'w')
	b = inf.read(1)
	while( b != ""):
		word = ord(b) + 5
		outf.write(chr(word))
		b = inf.read(1)

if(sys.argv[2] == 'decrypt'):
        outf = open(os.path.splitext(sys.argv[1])[0] + '.txt', 'w')
        b = inf.read(1)
        while( b != ""):
                word = ord(b) - 5
                outf.write(chr(word))
                b = inf.read(1)

if(sys.argv[2] == 'decrypt_script'):
        outf = open(os.path.splitext(sys.argv[1])[0] + '.py', 'w')
        b = inf.read(1)
        while( b != ""):
                word = ord(b) - 5
                outf.write(chr(word))
                b = inf.read(1)


#	for line in inf:
#		line = line.rstrip()
#		words = line.split()
#
#		for w in words:
#			word = ord(w)
#			outf.write(chr(word + 5))
	
	
