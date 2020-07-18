# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
from math import sqrt

def trianglearea(s1,s2,s3):
	s = (s1+s2+s3)/ 2
	a = sqrt( s * (s-s1)*(s-s2)*(s-s3))
	return a







def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = sqrt(((y2 - y1)**2) + ((x2-x1)**2))
	b = sqrt(((y3 - y2)**2) + ((x3-x2)**2))
	c = sqrt(((y3 - y1)**2) + ((x3-x1)**2))

	return trianglearea( a,b,c)


	# ahgkdskjgbajfsas