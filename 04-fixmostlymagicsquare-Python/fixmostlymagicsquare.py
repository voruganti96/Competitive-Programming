# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	
	# Your code goes here

	sum0 = sum(l[0])
	d = {}
	for i in L:
		if(sum(i) in d.keys()):
			d[sum(i)] +=1
		else:
			d[sum(i)] =1

	val = max(d.values())

	for j in d:
		if(d[j] == val):
			sum0=j
	
	for i in range(0, len(L)):
		if(sum(L[i]) != sum0):
			if(sum0 > sum(l[i])):
				l[i][-1] = L[i][-1]+ sum(sum0 - sum(L[i]))

			elif(sum0 < sum(L[i])):
				L[i][-1] = L[i][-1] - (sum(L[i])- sum0)


	return L