#!/usr/bin/python3.5

import sys

if(len(sys.argv) < 2):
	print('not enough arguments')
	sys.exit()

try:
	f = open(sys.argv[1], 'r')
except IOError:
	print('error opening the file')
	sys.exit()

array = []

for line in f:
	array.append(int(line))


#Now we merge sort our array

#first we need our recursive function

print('original')
print(array)


def merge_together(start, middle, end):
	#need to iterate through all elements and sort in place
	pass


def merge_sort(start, end):
	if((end-start) < 2):
		return
	#otherwise we have more than 2 elements, so break it in half
	middle = (start + end)/2
	
	merge_sort(start, middle)
	merge_sort(middle+1, end)
	
	#now we have arrays of 1 or 2 elements, so join and sort them

	merge_together(start, middle, end)

print('++++++')
print('final')
