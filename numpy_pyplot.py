#lIBRERIA Numpy

import numpy as np

# listas
lista1=[1,2,3,4,5]
lista2=[1,3.5,[3,5,7],'casa']
lista3=[3.5,4.7,2.2,7.9]
#print(type(lista1))

A=np.array([1,2,3,4,5,6]) # arreglo 1 dimension
B=np.array([[2,3,4,5],
            [2,1,5,5],
            [2,4,6,7]])# 2 dim

C=np.array([[[2,3,4], # 3 dim
            [2,1,5],
            [2,4,6]],
            [[2,3,4],
            [2,1,5],
            [2,4,6]]])
#print(C)
#print(A.ndim)
#print(B.ndim)
#print(C.ndim)
#print(A.shape)
#print(B.shape)
#print(C.shape)
#print(C.size)
#print(len(A))
#print(len(B))
#print(len(C))
#arreglos aleatorios
A=np.zeros([3,3,5])
A=np.ones([3,3,5])
A=np.full([3,4],5)
A=np.random.sample([2,4])
A=np.random.randint(1,10,size=[3,5])
A=np.random.uniform(1.5,20.5,size=[2,3])
# secuencias numericas
A=np.arange(1,30,3)
A=np.linspace(1,10,200)
#print(A)
lista1=[1,2,3,4,5]
lista2=[3,4,5,6,7]
A=np.array(lista1)
B=np.array(lista2)
#print(lista1-lista2)
#print(A*B)

# y=3x+2 [-5,5]
x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[-13,-10,-7,-4,-1,2,5,8,11,14,17]

def funcion_y(x):
    y=[]
    n=len(x)
    k=0
    while(k<n):
        y.append(3*x[k]+2)
        k+=1
    print("Coordenadas ejex=",x)
    print("Coordenadas ejey=",y)
    return(y)

def funcion_y2(x):
    y=3*x+2
    print(type(y))
    print("Coordenadas ejex=",x)
    print("Coordenadas ejey=",y)
    return(y)
    
#Casos de prueba
x=np.linspace(-5,5,5)
print(len(x))
funcion_y2(x)
    
    









