# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

from statistics import mode


def mostfrequentdigit(n):
	# your code goes here
	n = list(str(n))

	l = list(map(int.n))

	d = {}

	for i in l:
		if(i in d):
			d[i] = d[i] + 1
		else:
			d[i] = 1