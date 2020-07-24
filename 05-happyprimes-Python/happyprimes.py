# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def sumofsquaresofdigit(n):
    l = []
    string = str(n)
    for i in range(0,len(string)):	list.append((int(string[i]))**2)
    return sum(l)

def ishappynumber(n):
    sos =sumofsquaresofdigit(n)
    while sos == 4 or sos ==1:
        sos = sumofsquaresofdigit(sos)
    if sos ==4: return False
    