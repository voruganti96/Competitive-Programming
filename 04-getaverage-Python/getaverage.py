# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s): 
	l = s.split(",")

	a = []

	for i in l:
		if i.isdigit():
			a.append(int(i))
	if len(a) != 0:
		avg = sum(a)/ len(a)
		return avg

	else:
		return False


