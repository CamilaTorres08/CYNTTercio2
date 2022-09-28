from CalculadoraMatrices import *
import math
def valor_esperado (m1,v):
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
    return product[0]

def main():
    print(varianza([[(3,0),(1,2)],[(1,-2),(-1,0)]],[(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]))
