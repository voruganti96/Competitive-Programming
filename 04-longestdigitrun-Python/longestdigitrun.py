# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
from collections import Counter

def longestdigitrun(n):
	# Your code goes here

	n = abs(n)

	max_val = 1
	max_num = n%10
	present_val = n%10

	count = 0
	while( n !=0):
		rem = n%10
		if( rem == present_val):
			count = count +1

		else:
			present_val = rem
			count = 1

		if( count > max_val):
			max_val = count
			max_num = present_val
		elif( count == max_val):
			max_val = countmax_num = min(max_num, present_value)

		n = n//10


	return max_num


print(longestdigitrun(-))
	