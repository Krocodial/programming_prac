#!/usr/bin/python3.5

#Takes in data in one value per line from text file and sorts it

import sys

try:
	f = open(sys.argv[1], 'r')
except IOError:
	print("There was an error reading from the file")
	sys.exit()
numbers = []
for line in f:
	numbers.append(int(line))

def switch(a, b):
	c = tmp[a]
	tmp[a] = tmp[b]
	tmp[b] = c

tmp = numbers

print(numbers)
print('++++++++++++++++')

for i in numbers:
	for j in range(len(numbers)-1):
		if(numbers[j] < numbers[j+1]):
			print(str(numbers[j]) + ', ' + str(numbers[j+1]))
			switch(j, j+1)
	numbers = tmp

print(numbers)

f.close()
