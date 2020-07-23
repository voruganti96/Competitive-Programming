# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


all_factors = []

def fun_nth_smithnumber(n):
    present_number =0
    starting_number = 3

    while( present_number <= n):
        starting_number +=1
        all_factors.clear()

        if(verify(starting_number)):
            present_number += 1
    return starting_number


def verify(num):
    if(is_prime(num)):
        return False
    for i in range(2,num):
        if(is_prime(i) and num % i ==0):
            print(i)
            all_factors.append(i)

            if (num / i == float(i)):
                all_factors.append(i)

    result = 0

    for i in all_factors:
        while( i !=0):
            result += i% 10
            i = i //10

    num_result = 0
    while( num !=0):
        num_result += num %10
        num = num //10

    if(result == num_result):
        return True
    else:
        return False


all_primes = [2]

def is_prime(num):
    if(num in all_primes):
        return True
    for j in range(2,num):
        if (num % j ==0):
            return False
    all_primes.append(num)
    return True

