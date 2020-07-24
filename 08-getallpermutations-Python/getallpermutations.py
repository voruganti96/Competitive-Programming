# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
from itertools import permutations

def getallpermutations(s):
	# Your code goes here
	p_list = permutations(s)
	for p in p_list:
		print("".join(p))

p_list =  permutations("abc")