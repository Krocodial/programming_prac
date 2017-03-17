import sys

try:
	f = open('random.txt', 'r')
except FileNotFoundError:
	print("failed to open :)")
	sys.exit()
