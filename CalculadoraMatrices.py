from calculadoraComplejos import *
#from tabulate import tabulate

def SumVect(vect1,vect2):
    '''Esta función recibe como parámetro dos arreglos y, con ayuda de la libreria para calculadora de complejos,
        se realiza la suma con cada elemento correspondiente y retornar un vector con la suma'''
    sumav = []
    for i in range(len(vect1)):
        suma = SumComplex(vect1[i],vect2[i])
        sumav.append(suma)
    return sumav
def InversoVect (vect):
    '''Esta función recibe como parámetro un arreglo y, con ciclos de accede a cada elemento de la tupla
       para multiplicarla por -1 y cambiarles el signo y retornar un vector con el inverso'''
    for i in range(len(vect)):
        vect[i] = list(vect[i])
    for i in range(len(vect)):
        for j in range(len(vect[0])):
            n = vect[i][j] * (-1)
            vect[i][j] = n
    for i in range(len(vect)):
        vect[i] = tuple(vect[i])
    return vect
            
def MultEscalarVect (c,vect):
    '''Esta función recibe como parámetro una constante y un arreglo y, con ciclos se accede a cada elemento para multiplicarla por la variable c,
        y retornar un vector con la multiplicación'''
    for i in range(len(vect)):
        vect[i] = list(vect[i])
    for i in range(len(vect)):
        for j in range(len(vect[0])):
            n = vect[i][j] * c
            vect[i][j] = n
    for i in range(len(vect)):
        vect[i] = tuple(vect[i])
    return vect
def ProductInterVect(v1,v2):
    '''Esta función recibe como parámetro dos arreglos y, se llama desde el modulo para calculadora de complejos, la función de multiplicar y sumar,
        para retornar un valor con la suma'''
    suma = (0,0)
    adj = AdjuntaVect(v1)
    for i in range(len(v2)):
        b = MultComplex(adj[i],v2[i])
        suma = SumComplex(suma,b)
    return suma
def AdjuntaVect(v):
    '''Esta función recibe como parámetro unun arreglo y, con el modulo ConjComplex, calcula el conjugado de cada elemento y devuelve la adjunta del vector.'''
    adj = []
    for i in range(len(v)):
        adj.append(ConjComplex(v[i]))
    return adj
    
def SumMat (matr1,matr2):
    '''Esta función recibe como dos matrices, y con ciclos y la función SumComplex, se realiza la suma de cada elemento correspondiente,
        y retornar una matriz con la suma'''
    matriz = []
    lista = []
    for i in range(len(matr1)):
        for j in range(len(matr1[0])):
            suma = SumComplex(matr1[i][j],matr2[i][j])
            lista.append(suma)
        matriz.append(lista)
        lista = []
    return matriz
def restMat (matr1,matr2):
    '''Esta función recibe como dos matrices, y con ciclos y la función SumComplex, se realiza la suma de cada elemento correspondiente,
        y retornar una matriz con la suma'''
    matriz = []
    lista = []
    for i in range(len(matr1)):
        for j in range(len(matr1[0])):
            suma = RestComplex(matr1[i][j],matr2[i][j])
            lista.append(suma)
        matriz.append(lista)
        lista = []
    return matriz


def InversoMat (mat):
    '''Esta función recibe como parámetro una matrizy con ciclos se accede a cada elemento para multiplicarla por la variable -1,
        y retornar una matriz con el inverso'''
    for i in range(len(mat)): #Pasa la tupla a lista para poder modificarle los valores (parte entera y real)
        for j in range(len(mat[0])):
            mat[i][j] = list(mat[i][j])
        
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for u in range(len(mat[i][j])): #Calcula el inverso aditivo del complejo, cambia de signos la parte real e imaginaria
                n = mat[i][j][u]*(-1)
                mat[i][j][u] = n
    for i in range(len(mat)): #Vuelve a convertir la lista en tupla.
        for j in range(len(mat[0])):
            mat[i][j] = tuple(mat[i][j])

    return mat

def MultEscalarMat (c,m):
    '''Esta función recibe como parámetro una constante y una matriz y, con ciclos se accede a cada elemento para multiplicarla por la variable c,
        y retornar una matriz con la multiplicación'''
    for i in range(len(m)): #Pasa la tupla a lista para poder modificarle los valores (parte entera y real)
        for j in range(len(m[0])):
            m[i][j] = list(m[i][j])
        
    for i in range(len(m)):
        for j in range(len(m[0])):
            for u in range(len(m[i][j])): #Multiplica cada elemento por el escalar
                n = m[i][j][u]*c
                m[i][j][u] = n
    for i in range(len(m)): #Vuelve a convertir la lista en tupla.
        for j in range(len(m[0])):
            m[i][j] = tuple(m[i][j])
    return m
            
def TraspuestaMat (m):
    '''Esta función recibe como parámetro una matriz y cambia las filas por las columnas y retorna la traspuesta de la matriz'''
    mat=[]
    for j in range(len(m[0])):
        lista = []
        for i in range(len(m)):
            lista.append(m[i][j])
        mat.append(lista)
    return mat

        
def ConjugadoMat (m):
    '''Esta función recibe como parámetro una matriz, y se hace uso de la funcion ConjComplex para calcular el conjugado de cada elemento,
        y retornar una matriz conjugada'''
    mat=[]
    for i in range(len(m)):
        lista = []
        for j in range(len(m[0])):
            lista.append(ConjComplex(m[i][j]))
        mat.append(lista)
    return mat
def AdjuntaMat (m):
    '''Esta función recibe como parámetro una matriz y se hace uso de las funciones TraspuestaMat y ConjugadoMat
        para retornar la adjunta de la matriz'''
    matr = ConjugadoMat(m)
    matriz = TraspuestaMat(matr)
    return matriz

def ProductMat(m1,m2):
    '''Esta función recibe como parámetro dos matrices, y con ciclos se calcula la multiplicacion y suma de fila
        por columna con la función MultComplex y SumComplex
        y retorna una con la multiplicación'''
    mat = []
    for i in range(len(m1)):
        k = 0
        mult = []
        while k < len(m2[0]):
            suma = (0,0)
            for j in range(len(m2)):
                m = MultComplex(m1[i][j],m2[j][k])
                suma = SumComplex(suma,m)
            k = k + 1
            mult.append(suma)
        mat.append(mult)
    return mat
def NormVect(vect):
    '''Esta función recibe como parámetro un arreglo y, se hace uso de la funcion para producto interno para retorna la raiz
        del producto interno'''
    n = ProductInterVect(vect,vect)
    return math.sqrt(n[0])
def distanciaVect(v1,v2):
    '''Esta función recibe como parámetro dos arregloa y, se hace uso de la funcion RestComplex para restar ambos vectores
        y luego hacer uso de la funcion para la norma de un vector y retornar la distancia.'''
    restav = []
    for i in range(len(v1)):
        resta = RestComplex(v1[i],v2[i])
        restav.append(resta)
    d = NormVect(restav)
    return d
def EsUnitaria (m):
    '''Esta función recibe como parámetro una matriz y calcula la adjunta para luego hacer uso de la funcion del producto entre matrices.
        Luego, compara cada elemento del producto con 1 y si la cantidad de 1 es igual a la dimensión del producto entre las matrices, se
        retorna verdadero.'''
    adj = AdjuntaMat(m)
    product = ProductMat(m,adj)
    cant = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                if round(product[i][j][0],1) == 1.0:
                    cant += 1
    if cant == (len(product)):
        return True
    else:
        return False
def EsHermitiana (m):
    '''Esta función recibe como parámetro una matriz y se calcula su adjunta, si cada elemento de ambas matrices son iguales, se acumula la cantidad
        de veces en que estas son iguales, y si la cantidad es igual a la dimension de las matrices, se retorna verdadero.'''
    adj = AdjuntaMat(m)
    igual = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == adj[i][j]:
                igual += 1
    if igual == (len(m)*len(m[0])):
        return True
    else:
        return False

def ProductTensor(m1,m2):
    '''Esta función recibe como parámetro dos matrices o vectores y multiplica cada elemento de la matriz 1 con la matriz 2 con la funcion MultComplex y retorna una
        matriz con la multiplicacion de cada elemento con la otra matriz'''
    t = []
    producT=[]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            k = 0
            while k < len(m2):
                ml = []
                for p in range(len(m2[0])):
                    mult = MultComplex(m1[i][j],m2[k][p])
                    ml.append(mult)
                producT.append(ml)
                k += 1
    
    return producT

def Imprimir_Vectores(vect):
    '''Esta función recibe como parámetro un vector y con el modulo para imprimir los numeros complejos de una manera mas "formal",
        se imprime cada elemento del vector'''
    print('-------')
    for i in vect:
        PrintNumsCart(i)
    print('-------')
    print('\n')

def main():    
    print("=======================VECTORES====================")
    print("SUMA +: ")
    Imprimir_Vectores(SumVect([(1,2),(3,4)],[(3,4),(6,7)]))
    print("INVERSO ADITIVO: ")
    Imprimir_Vectores(InversoVect([(1,2),(3,4)]))
    print("MULTIPLICACIÓN POR ESCALAR: ")
    Imprimir_Vectores(MultEscalarVect(3,[(1,2),(3,4)]))
    print("PRODUCTO INTERNO: ")
    print(ProductInterVect([(1,2),(3,4)],[(3,4),(6,7)]),'\n')
    print("ADJUNTA: ")
    Imprimir_Vectores(AdjuntaVect([(1,2),(3,4)]))
    print("NORMA: ")
    print(NormVect([(1,2),(3,4)]),'\n')
    print("DISTANCIA: ")
    print(distanciaVect([(1,2),(3,4)],[(3,4),(6,7)]),'\n')
    print("=======================MATRICES====================")
    #Con el modulo tabulate, se imprime de una manera más ordenada la matríz
    print("SUMA +: ")
    print(tabulate(SumMat([[(1,2),(3,4),(5,1)]],[[(6,7),(8,9),(10,3)]])),'\n')
    print("INVERSO ADITIVO: ")
    print(tabulate(InversoMat([[(1,2),(3,4),(5,1)],[(6,7),(8,9),(10,3)]])),'\n')
    print("MULTIPLICACION POR ESCALAR: ")
    print(tabulate(MultEscalarMat(3,[[(1,2),(3,4),(5,1)],[(6,7),(8,9),(10,3)]])),'\n')
    print("TRASPUESTA: ")
    print(tabulate(TraspuestaMat([[(1,2),(3,4),(5,1)],[(6,7),(8,9),(10,3)]])),'\n')
    print("CONJUGADA: ")
    print(tabulate(ConjugadoMat(([[(1,2),(3,4),(5,1)],[(6,7),(8,9),(10,3)]]))),'\n')
    print("ADJUNTA: ")
    print(tabulate(AdjuntaMat(([[(1,2),(3,4),(5,1)],[(6,7),(8,9),(10,3)]]))),'\n')
    print("PRODUCTO ENTRE MATRICES: ")
    print(tabulate(ProductMat([[(1,2),(3,4),(10,-11)],[(4,5),(6,7),(12,4)]],[[(1,2),(3,4),(7,8),(-4,-6)],[(7,0),(0,1),(0,4),(7,10)],[(0,2),(4,0),(-1,-1),(0,-1)]])),'\n')
    print("¿ES UNITARIA?: ")
    if EsUnitaria([[(1/2,1/2),(1/2,-1/2)],[(1/2,-1/2),(1/2,1/2)]]):
        print("La matriz dada es unitaria",'\n')
    else:
        print("La matriz dada no es unitaria",'\n')
    print("¿ES HERMITANIA?: ")
    if EsUnitaria([[(1/2,1/2),(1/2,-1/2)],[(1/2,-1/2),(1/2,1/2)]]):
        print("La matriz dada es hermitana",'\n')
    else:
        print("La matriz dada no es herminatana",'\n')

    print("PRODUCTO TENSOR: ")
    print(tabulate(ProductTensor([[(1,2),(3,4),(5,1)],[(1,1),(2,2),(3,3)]],[[(6,7),(8,9),(10,3)],[(1,2),(-3,3),(4,5)]])),'\n')
    

