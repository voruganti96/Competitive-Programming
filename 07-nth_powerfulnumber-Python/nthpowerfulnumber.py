def primefactors(p):
	list1 = []
	while(p%2 == 0):
		list1.append(2)
		p = p//2
	for i in range(3, p//2+1, 2):
		while(p%i == 0):
			list1.append(i)
			p = p//i
	if(p>2):
		list1.append(p)
	return list1

print(primefactors(36))

def powerfull(n):
	checklist = primefactors(n)
	for i in checklist:
		if(n % i**2 != 0):
			return False
	return True


def nthpowerfulnumber(n):
	# Your code goes here
	val = 1
	count = -1
	while(count < n):
		if(powerfull(val)):
			count += 1
			if(count == n):
				return val
		val += 1

	
print(nthpowerfulnumber(4))