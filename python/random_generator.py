#!/usr/bin/python3.5

import sys
import random

f = open('test_data.txt', 'w')
i = 30
j = 40
if(len(sys.argv) > 1):
	i = int(sys.argv[1])	

if(len(sys.argv) > 2):
	j = int(sys.argv[2])

#f.write('89\n87')
for i in range(i):
	f.write(str(random.randrange(j)) + '\n')

