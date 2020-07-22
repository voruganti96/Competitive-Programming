# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}

	for i in s:
		if i in d:
			d[i] = d[i] +1
		else:
			d[i]= 1


	l = sorted(d.items(), key = lambda x: x[1], reverse= True)

	return l[n-1][0]



		
