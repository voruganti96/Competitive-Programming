# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

primes = []
nonprimes =[]
def is_prime(n):
	if n < 1 or n % 1 >0 or n==4:
		return False

	for i in range(2,n//2):
		if n % i == 0:
			return False	
	return True

def sum_digits(n):
	sum=0
	for digit in str(n):
		sum += int(digit)
	print(sum)

def prime_list():
	for i in range(2,100):
		if is_prime(i) == True:
			primes.append(i)
		else:
			nonprimes.append(i)
prime_list()

def is_additiveprime():
	for i in primes:
		if sum_digits(i) 
	pass

def fun_nth_additive_prime(n):
	
	return 1


sum_digits(25)
print(is_prime(4))


