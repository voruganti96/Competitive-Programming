# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
\
def isprime(n):
	i = 1
	c = 0

	while(i <=n):
		if( n% i ==0):
			c += 1
			if(c >2):
				break
		i +=1

	if(c <=2):
		return True

	return False


def iscircularprime(n):
	if(n ==0):
		return False
	c = 0
	temp = n
	while( temp !=0):
		temp //= 10
		c +=1
	
	for i in range(c):
		if not isprime(n):
			return False

		rotated = n
		c1 = 0
		while( rotated !=0):
			rotated //=10
			c1 += 1

		rem = n%10
		num = n//10
		n = rem*(10**(c1-1))+ num
	return True




def nthcircularprime(n):
	# Your code goes here
	num = 1
	 c = 0
	 