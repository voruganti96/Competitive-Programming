# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.



def isprime(n):
	if n <=1:
		return False

	for i in range(2,n//2+1):
		if n% i ==o:
			return False
		else:
			return True

def fun_hasnoprimes(l):
	return True

