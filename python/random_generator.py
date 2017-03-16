#!/usr/bin/python3.5

import random

f = open('test_data.txt', 'w')

#f.write('89\n87')
for i in range(50):
	f.write(str(random.randrange(30)) + '\n')

