# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    low = n -math.floor(n)
    high = math.ceil(n) -n
    if(iskaprekarnumber(n)):
        return n

    m = n-low
    s = n+high
    while True:
        if(iskaprekarnumber(m)):
            if(iskaprekarnumber(s)):
                if(abs(s-n) < abs(m-n)):
                    return s
                    break
                else:
                    return m
                    break
            else:
                return m
                break
        if(iskaprekarnumber(s)):
            return s
            break
        m -=1
        s +=1


def iskaprekarnumber(n):
    if(n==0):
        return 1
    num = int(n**2)
    x =0
    y = num
    while(y >0):
        x +=1
        y //=10
    for j in range(x):
        temp = num//(10**j)
        r = num%(10**j)
        if (r !=0)
