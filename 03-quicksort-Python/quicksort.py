"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	qsort(array,0,len(array)-1)
	return array

def qsort(array, start, end):
	if start < end:

		part = partition(array, start, end)
		qsort(array, start , part-1)
		qsor