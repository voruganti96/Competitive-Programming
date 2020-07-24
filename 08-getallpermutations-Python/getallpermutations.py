# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
from itertools import permutations

def getallpermutations(str):
	# Your code goes here
	list = []
	p_list = permutations(str)
	for p in p_list:
		list.append(p)
	print(list)

getallpermutations("abc")