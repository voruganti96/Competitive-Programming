# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
	# your code goes here
	num = 1

	i = 1

	while( i <= n):
		if(islychrel(i)):
			i = i +1

		num = num +1

	print(num -1)
	return num-1

def islychrel(num):
	max_iteration = 20
	for i in range(max_iteration):
		num = num +reverse(num)
		if(num == reverse(num)):
			return False

	return True

def reverse(num):
	rev = 0

	while(num > 0):
		rem = num %10
		rev = (rev *10) + rem
		num //=10

	return rev

# print(nthlychrelnumbers(1))