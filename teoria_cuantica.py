from CalculadoraMatrices import *
from calculadoraComplejos import *
def verificar_normalizado(v):
    suma = 0
    for i in v:
        suma += (ModComplex(i)**2)
    if suma == 1:
        return True
    else:
        return False
def normalizar (v):
    vect = []
    mod = NormVect(v)**2
    if verificar_normalizado(v):
        return v
    else:
        vect = MultEscalarVect((1/NormVect(v)),v)
        return vect
    
def probabilidad (v,x):
    ve = normalizar(v)
    vect = NormVect(ve)
    pos = ModComplex(v[x])
    prob = (pos**2)/(vect**2)
    p = prob * 100
    return p

def amplitud(vect1,vect2):
   
    amp = ProductInterVect(vect2,vect1)
    print(amp)
    prob = ModComplex(amp)**2
    return prob
    
def main():
    #print(probabilidad([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],7))
    print(amplitud([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]))
