# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	l = list(str(n)[::-1])
	try:
		if l[k] in "0123456789":
			l[k] = str(d)
		elif l[k] in "-":
			l[k] = str(d)
			l.append("-")
		return int("".join(l[::-1]))
	
	except:
		l.append(str(d))
		return int(''.joint(l[::]))

