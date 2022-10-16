from CalculadoraMatrices import *
import numpy as np
import math
def unitaria (mat):
    if EsUnitaria(mat):
        return True
    else:
        return False
        
def dinamica (mat,v,clicks):
    for time in range(clicks):
        mult = []
        for i in range(len(mat)):
            suma = (0,0)
            for j in range(len(mat[0])):
                m = MultComplex(mat[i][j],v[j])
                suma = SumComplex(suma,m)
            mult.append(suma)
        v = mult
    return v
def main():
    print(unitaria([[(0,0),(1,0)],[(1,0),(0,0)]]))
    print(unitaria([[(math.sqrt(2)/2,0),(math.sqrt(2)/2,0)],[(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]]))
    product = ProductMat([[(0,0),(1,0)],[(1,0),(0,0)]],[[(math.sqrt(2)/2,0),(math.sqrt(2)/2,0)],[(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]])
    print(unitaria(product))
    print(dinamica([[(0,0),(1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0)],[(0,1/math.sqrt(2)),(0,0),(0,0),(1/math.sqrt(2),0)
],[(1/math.sqrt(2),0),(0,0),(0,0),(0,1/math.sqrt(2))],[(0,0),(1/math.sqrt(2),0),(-1/math.sqrt(2),0),(0,0)]],[(1,0),(0,0),(0,0),(0,0)],3))   
