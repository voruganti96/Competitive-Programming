# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	l = [[1], [1,1]]
	for i in range(2,row+1):
		a = []
		a.append(l[-1][0])
		for j in range(len(l[-1])-1):
			a.append(l[-1][j]+l[-1][j+1])
		a.append(l[-1][-1])
		l.append(a)
	

	try:
		return l[row][col]
	except:
		return 0
	