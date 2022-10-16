from CalculadoraMatrices import *
import numpy as np
import math
def valor_esperado (m1,v):
    '''Esta función recibe una matriz hermitiana y un vector y calcula el vector esperado'''
    if EsHermitiana(m1):
        mat = []
        mult = []
        for i in range(len(m1)):
            suma = (0,0)
            for j in range(len(m1[0])):
                m = MultComplex(m1[i][j],v[j])
                suma = SumComplex(suma,m)
            mult.append(suma)
        inter = ProductInterVect(mult,v)
        return inter
def varianza (m,v):
    '''Esta función recibe una matriz hermitiana y un vector y calcula la varianza'''
    valor = valor_esperado (m,v)
    identica = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            if j == i:
                fila.append((1,0))
            else:
                fila.append((0,0))
        identica.append(fila)
    multi = MultEscalarMat(valor[0],identica)
    delta = restMat(m,multi)
    multmat = ProductMat(delta,delta)
    mult = []
    for i in range(len(multmat)):
            suma = (0,0)
            for j in range(len(multmat[0])):
                m = MultComplex(multmat[i][j],v[j])
                suma = SumComplex(suma,m)
            mult.append(suma)
    product = ProductInterVect(mult,v)
    return product
def valores__vectores_propios(mat):
    '''Esta función recibe una matriz y devuelve los valores y vectores propios usando numpy'''
    valores,vectores = np.linalg.eig(mat)
    return valores,vectores
def probabilidad_sistema_eigenvalue(mat,sistem):
    '''Esta función calcula la probabilidad de que un sistema tansite a alguno de los vectores propios, devulve un arreglo con la probabilidades'''
    val,vect = valores__vectores_propios(mat)
    probabilidades = []
    for i in range(len(vect)):
        prob = abs(np.dot(sistem,vect[i]))
        probabilidades.append(prob)
    return probabilidades
    

def main():
    '''Función principal, contiene casos de prueba'''
    print(valor_esperado([[(0,0),(0,-1)],[(0,1),(0,0)]],[(1/math.sqrt(2),0),(0,1/math.sqrt(2))]))
    print(varianza([[(0,0),(0,-1)],[(0,1),(0,0)]],[(1/math.sqrt(2),0),(0,1/math.sqrt(2))]))
    valor,vector = valores__vectores_propios([[0,1],[1,0]])
    print(vector)
    print(probabilidad_sistema_eigenvalue([[-1,-1j],[1j,1]],[1/2,1/2]))
