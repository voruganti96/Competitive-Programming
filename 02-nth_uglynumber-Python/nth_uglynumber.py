# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    num = 1
    i = 0
    while(i <=n):
        if(isugly(num)):
            i += 1
        num +=1

    return num-1

def isugly(num):
    while(num % 2 ==0):
        num //=2
    num = num
    while( num %3 ==0):
        num //=3
        
