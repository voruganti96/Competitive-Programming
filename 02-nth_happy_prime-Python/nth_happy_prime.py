# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).





def ishappynumber(n):
	if n ==1:
		return True
	elif n <= 0 or n ==4:
		return False

	else:
		s = 0
		rem = 0
		while ( n > 0):
			rem = n %  10
			s = s + rem()**2
			n = n//10

		return ishappynumber(s)


def isprime(n):
	flag = 0
	for i in range(1, n+1,1):
		if n % i ==0:
			flag = flag +1
	if flag ==2:
		return True
	else:
		return False


def fun_nth_happy_prime(n):
	count = 1
	while n >= 0:
		if ishappynumber(count) and isprime(count):
			n = n-1
			count = count +1

	return count -1