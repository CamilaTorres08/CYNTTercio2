import matplotlib.pyplot as plt
import seaborn as sns
def coeficiente_booleano(m,m2):
    '''Función para calcular la multiplicacion entre matrices, especialmente las booleanas'''
    mat = []
    for i in range(len(m)):
        k = 0
        s = []
        while k < len(m[0]):
            suma = 0
            for j in range(len(m2)):
                mult = m[i][j]*m2[j][k]
                suma = suma + mult
            s.append(suma)
            k = k + 1
        mat.append(s)
    return mat

def calcular_clicks(m,n):
    '''Función que me calcula la posicion de las canicas despues de un tiempo n'''
    h = 0
    m2 = m
    while h < n-1:
        m = coeficiente_booleano(m,m2)
        h += 1
    return m
    
def Probabilidad_Multi (m,x):
    '''Calcula la probabilidad de las posiciones de las canicas pasandole la matriz de
        proximidad y el vector x para que retorne el vector Y que tiene la probabilidad'''
    mat = []
    mult = []
    for i in range(len(m)):
        j = 0
        suma = 0
        while j < len(m[0]):
            mt = m[i][j]*x[j]
            suma += mt
            j = j + 1

        mult.append(suma)
    return mult

def mult_rendijas(m,n):
    '''recibe la matriz de continuidad M y la matriz de continuida N, realiza el
        producto tensor para calcular el estado de las dos canicas'''
    t = []
    producT=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            k = 0
            while k < len(n):
                ml = []
                for p in range(len(n[0])):
                    mult = m[i][j]*n[k][p]
                    ml.append(mult)
                producT.append(ml)
                k += 1
    return producT

x = ['R','Python','Scala','SQL']
y = [456,899,500,345]
plt.bar(x,y)
plt.title("Estados de las canicas despues de un tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Estado")
plt.show()
print(calcular_clicks([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]],6))
print(Probabilidad_Multi ([[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]],[1/6,1/6,2/3]))
print(mult_rendijas([[0,1,2],[1,2,3],[4,5,6]],[[1,2],[3,4]]))

'''[[0,0,0,0],
    [0,0,0,0],
    [0,1,0,0],
    [1,1,1,1]]'''
