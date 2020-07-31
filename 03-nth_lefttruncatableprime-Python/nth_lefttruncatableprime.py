# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def isprime(n):
    if(n==1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True

def lefttruncate(n):
    l1 = []
    while n >0:
        l1.append(str(n%10))
        n = n//10
    for i in range(len(l1)-1,-1,-1):
        check = "".join(l1[i::-1])
        if(not isprime(int(check)) or "0" in check):
            return False
    ret



def fun_nth_lefttruncatableprime(n):
    return 1