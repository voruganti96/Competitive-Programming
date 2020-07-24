# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	present_num = 0
	starting_num = 1

	while present_num <= n:
		result = str(starting_num **5)

		flag = False

		for i in digits:
			if i not in result:
				flag = True
				break

		if(not flag):
			present_num += 1
		starting_num += 1

	