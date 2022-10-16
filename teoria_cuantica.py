from CalculadoraMatrices import *
from calculadoraComplejos import *
import math
def verificar_normalizado(v):
    '''Recibe un arreglo y llama a la función para calcular la norma y devuelve True si es 1'''
    norm = NormVect(v)
    if norm == 1:
        return True
    else:
        return False
def normalizar (v):
    '''Si la norma no es 1, hace la multiplicacion de cada elemento del arreglo por 1/norma para normalizarlo'''
    div = 1/NormVect(v)
    if verificar_normalizado(v):
        return v
    else:
        vect = MultEscalarVect(div,v)
        return vect
    
def probabilidad (v,x):
    '''Esta función recibe un vector y la posición en la que se quiere saber la probabilidad y devuelve el valor de la probabilidad'''
    ve = normalizar(v)
    vect = NormVect(ve)
    pos = ModComplex(v[x])
    prob = (pos**2)/(vect**2)
    p = prob * 100
    return p

def amplitud(vect1,vect2):
    '''Esta función recibe el vector de incio y el vector de fin para calcular cual es la amplitud de transitar de uno a otro'''
    vect1_norm = normalizar (vect1)
    vect2_norm = normalizar (vect2)
    amp = ProductInterVect(vect2_norm,vect1_norm)
    return amp
    
def main():
    print("La probabilidad es:",probabilidad([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],7))
    print("La amplitud es: ",amplitud([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]))
    print("La amplitud es: ",amplitud([(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]))
