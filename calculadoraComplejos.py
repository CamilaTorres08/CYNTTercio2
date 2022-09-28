#Calculadora de numeros complejos
import math

def SumComplex (numero1,numero2): 
    real = numero1[0]+numero2[0]
    imag = numero1[1]+numero2[1]
    return (real,imag)
def MultComplex (numero1,numero2):
    real = numero1[0]*numero2[0] - numero1[1]*numero2[1]
    imag = numero1[0]*numero2[1] + numero1[1]*numero2[0]
    return (real,imag)
def RestComplex (numero1,numero2):
    real = numero1[0]- numero2[0]
    imag = numero1[1] - numero2[1]
    return (real,imag)
def DivComplex (numero1,numero2):
    result1 = numero1[0]*numero2[0]+numero1[1]*numero2[1]
    result2 = (numero2[0]**2)+(numero2[1]**2)
    result3 = numero2[0]*numero1[1] - numero1[0]*numero2[1]
    return (result1//result2,result3//result2)
def ModComplex (numero):
    a = numero[0]**2
    b = numero[1]**2
    return math.sqrt(a+b)
def ConjComplex (numero):
    return (numero[0],numero[1]*-1)
def PolCartComplex (numero): #Convierte de polar a cartesiano
    a = numero[0]*math.cos(numero[1])
    b = numero[0]*math.sin(numero[1])
    return (a,b)
def CartPolComplex (numero): #Convierte de cartesiano a polar
    p = ModComplex(numero)
    ang = FaseComplex(numero)
    return (p,ang)
def FaseComplex (numero): #Halla la fase del complejo
    return math.atan2(numero[1],numero[0])
def PrintNumsCart (c): #Imprime numeros cartesianos
    real = str(c[0])
    img = str(c[1])
    if c[1] < 0:
        print(real,img,"i",sep="",end='\n')
    else: 
        print(real,"+",img,"i",sep="",end='\n')
def PrintNumsPol (c): #Inprime numeros polares
    print(str(c[0]),"e^(i" ,str(c[1]),")")
def main():
    print("Suma:", end= " ")        
    PrintNumsCart(SumComplex((2,3),(4,7)))
    print("Multiplicación:", end= ' ')
    PrintNumsCart(MultComplex((2,3),(4,7)))
    print("Resta:",end= ' ')
    PrintNumsCart(RestComplex((3,-1),(1,4)))
    print("División:",end= ' ')
    PrintNumsCart(DivComplex((-2,1),(1,2)))
    print("Módulo:",end= ' ')
    print(ModComplex((1,-1)))
    print("Conjugado:",end= ' ')
    PrintNumsCart(ConjComplex((3,2)))
    print("Polar a cartesiano:",end= ' ')
    PrintNumsCart(PolCartComplex((3,-1)))
    print("Cartesiano a polar:",end= ' ')
    PrintNumsPol(CartPolComplex((-3,-2)))
    print("Fase:",end= ' ')
    print(FaseComplex((-3,-2)))
