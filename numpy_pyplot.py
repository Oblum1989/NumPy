#lIBRERIA Numpy

import numpy as np
import matplotlib.pyplot as plt


# listas
lista1=[1,2,3,4,5]
lista2=[1,3.5,[3,5,7],'casa']
lista3=[3.5,4.7,2.2,7.9]
A=np.array([[2,3,4,7],[1,6,7,9],[1,4,7,9]])

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
A=np.full((3,4),5)
#print(A)
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
#x=np.linspace(-5,5,5)
#print(len(x))
#funcion_y2(x)


# GRAFICA DE FUNCIONES


def funcion_lineal(x,m,b):
    y=m*x+b
    print("Coordenadas ejex=",x)
    print("Coordenadas ejey=",y)
    return(y)

#Casos de pruba
#x=np.linspace(-5,5,11)# crea una secuancia numerica [-5,-4,-3,-2,-1,0,1,2,3,4,5]
#funcion_lineal(x,-5,-3)   # y= -5x-3
#funcion_lineal(x,4,3)   # y= 4x+3
#funcion_lineal(x,2,0)   # y= 2x

def funcion_exponencial(x,a,b):
    y=a*np.e**(b*x)
    return(y)
 
def funcion_seno(x,a,b):
    y=a*np.sin(b*x)
    return(y)
def funcion_coseno(x,a,b):
    y=a*np.cos(b*x)
    return(y)

def funcion_logaritmo(x,a,b):
    y=a*np.log(x)+b
    return(y)

def graficar_funcion_lineal(j,k,n,m,b,num):
    ventana=plt.figure(num)# objeto
    plano=ventana.gca() # superficie de dibujo
    x=np.linspace(j,k,n)
    y=funcion_lineal(x,m,b)
    plano.plot(x,y,'h--c',label='y=mx+b')
    plano.legend(loc=2)
    plano.set_title(label='Funcion Lineal', color='r', size=20)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.spines['bottom'].set_position('zero')
    plano.spines['left'].set_position('zero')
    plano.set_xlabel(xlabel='eje x',labelpad=200)
    plano.set_ylabel(ylabel='eje y',labelpad=300 )
    plano.set_xticks([-3,3])
    return(ventana)
    

#casos de prueba
#graficar_funcion_lineal(-3,3,7,2,0,1) # y=2x
#graficar_funcion_lineal(-3,3,7,-2,0,1) # y=-2x
#plt.show()

def graficar_funcion_exponencial(j,k,n,a,b,num):
    ventana=plt.figure(num)# objeto
    plano=ventana.gca() # superficie de dibujo
    x=np.linspace(j,k,n)
    y=funcion_exponencial(x,a,b)
    plano.plot(x,y)
    plano.set_xlabel(xlabel='eje x',labelpad=10)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.spines['bottom'].set_position('zero')
    plano.spines['left'].set_position('zero')
    return(ventana)
    
#Casos de prueba
#graficar_funcion_exponencial(-20,100,100,-2,0.1,1) # y= 2*e**(0.1x)
#graficar_funcion_lineal(-20,100,7,1000,0,2)
#plt.show()

def graficar_funcion_seno(j,k,n,a,b,num):
    ventana=plt.figure(num)# objeto
    plano=ventana.gca() # superficie de dibujo
    x=np.linspace(j,k,n)
    y=funcion_seno(x,a,b)
    plano.plot(x,y)
    #plano.set_xlabel(xlabel='eje x',labelpad=10)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.spines['bottom'].set_position('zero')
    plano.spines['left'].set_position('zero')
    return(ventana)

# casos de prueba
#graficar_funcion_seno(-2*np.pi,2*np.pi,100,1,1,1) # y= sen(x)
#plt.show()

def graficar_funcion_coseno(j,k,n,a,b,num):
    ventana=plt.figure(num)# objeto
    plano=ventana.gca() # superficie de dibujo
    x=np.linspace(j,k,n)
    y=funcion_coseno(x,a,b)
    plano.plot(x,y)
    #plano.set_xlabel(xlabel='eje x',labelpad=10)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.spines['bottom'].set_position('zero')
    plano.spines['left'].set_position('zero')
    return(ventana)
# casos de prueba
#graficar_funcion_seno(0,2*np.pi,100,1,1,1) # y= sen(x)
#graficar_funcion_coseno(-2*np.pi,2*np.pi,100,2,1,1) # y= cos(x)
#plt.show()


def graficar_funcion_logaritmo(j,k,n,a,b,num):
    ventana=plt.figure(num)# objeto
    plano=ventana.gca() # superficie de dibujo
    x=np.linspace(j,k,n)
    y=funcion_logaritmo(x,a,b)
    plano.plot(x,y)
    #plano.set_xlabel(xlabel='eje x',labelpad=10)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.spines['bottom'].set_position('zero')
    plano.spines['left'].set_position('zero')
    return(ventana)

# casos de prueba
graficar_funcion_logaritmo(0.1,100,100,1,-1,1) # y= ln(x)
plt.show()







