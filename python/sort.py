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


def merge_sort(array):
	if(len(array) < 2):
		return
	#otherwise we have more than 2 elements, so break it in half
	middle = len(array)//2
	
	lefthalf = array[:middle]
	righthalf = array[middle:]

	merge_sort(lefthalf)
	merge_sort(righthalf)
	
	#We are left with 2 arrays of varying length that are sorted
	i = 0
	j = 0
	k = 0

	while(i != len(lefthalf) and j != len(righthalf)):
		if(lefthalf[i] > righthalf[j]):
			array[k] = lefthalf[i]
			i += 1
		else:
			array[k] = righthalf[j]
			j += 1
		k+=1
	while(i != len(lefthalf)):
		array[k] = lefthalf[i]
		i+=1
		k+=1
	while(j != len(righthalf)):
		array[k] = righthalf[j]
		j+=1
		k+=1





		
	
	#now we have arrays of 1 or 2 elements, so join and sort them



print('++++++')
print('final')
merge_sort(array)
print(array)
