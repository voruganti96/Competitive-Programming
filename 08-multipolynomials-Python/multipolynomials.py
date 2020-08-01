# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].
# from numpy.polynomial import polynomial as poly
# import numpy as np

def multipolynomials(p1, p2):
	# Your code goes here
	# p1=np.poly1d(p1)
	# p2=np.poly1d(p2)
	# print("P1:\n",p1)
	# print("P2:\n",p2)
	# res_poly = poly.polymul(p1,p2)
	# int_res=[]
	# for i in res_poly:
	# 	int_res.append(int(i))
	# return int_res

	m = len

	

#multipolynomials(p1,p2)
#print(multipolynomials(p1,p2))
