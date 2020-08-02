# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.
import numpy as np

def fun_matrixmultiply(m1, m2):
    # for i in m1:
    #     if len(i) !=len(m2):
    #         return None
    

    # result = []
    # for i in range(len(m1)):
    #     l = []
    #     for j in range(len(m2[0])):
    #         x = 0
    #         for k in range (len(m2)):
    #             x += m1[i][k] * m2[k][j]

    #             l.append(x)

    #     result.append(l)

    # return result

    # # # Done
    # # '''
    # # ksdjfkdzf
    # # '''

    rows1 = len(m1)
    rows2= len(m2)
    col1= len(m1[0])
    col2=len(m2[0])



