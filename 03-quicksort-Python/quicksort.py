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
		qsort(array, part+1 , end)


def partition(array, start, end):
	pivot = start+1
	high = end
	while True:
		while low <= high and array[high] >= pivot:
			high = high -1
		while low <= high and array[low] <= pivot:
			low = low+1
		if low <= high:
			array[low],array[high],array[low]
		else:
			break

	array[start] , array[high] = array[high] , array[start]
	return high
