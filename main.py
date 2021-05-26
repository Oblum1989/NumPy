#lIBRERIA Numpy

import numpy as np
import matplotlib.pyplot as plt

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
    #print(type(y))
    print("Coordenadas ejex=",x)
    print("Coordenadas ejey=",y)
    return(y)
    
#Casos de prueba
#x=np.linspace(-5,5,5)
#print(x)
#print(len(x))
#funcion_y2(x)
#
#
#
#t = np.arange(0.0, 2.0, 0.01)
#s = 1 + np.sin(2*np.pi*t)
#plt.plot(t, s)
#
#plt.xlabel('time (s)')
#plt.ylabel('voltage (mV)')
#plt.title('About as simple as it gets, folks')
#plt.grid(True)
#plt.savefig("test.png")
#plt.show()
#ventana = plt.figure()
#plano = ventana.gca()
#plano.plot(x, funcion_y(x))
#plt.show()

def ejercicio_1(a,x):
  y=a*x**3*np.sin(x**2)
  return(y)

def grafica_ejercicio_1 (j,k,n,a,num):
  ventana=plt.figure(num)
  plano=ventana.gca() 
  x=np.linspace(j,k,n)
  y=ejercicio_1(a,x)
  plano.plot(x,y,'.--m',label='y=a*x**3*sin(x**2)')
  plano.legend(loc=2)
  plano.set_title(label='Ejercicio 1', color='c', size=20)
  plano.set_xlabel(xlabel='eje x',labelpad=230)
  plano.set_ylabel(ylabel='eje y',labelpad=450)
  plano.spines['top'].set_visible(False)
  plano.spines['right'].set_visible(False)
  plano.spines['bottom'].set_position('zero')
  plano.spines['left'].set_position('zero')
  plano.set_xticks([-3.14,3.14])
  return(ventana)

#grafica_ejercicio_1(-3.14,3.14,100,0.1,1)
#plt.show()

def funcion_lineal(x,m,b):
  y=m*x+b
  print("Coordenadas ejex=",x)
  print("Coordenadas ejey=",y)
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


def graficar_varias_funciones():
  ventana=plt.figure()
  plano=ventana.add_gridspec (1,2)
  plano1=ventana.add_subplot(plano[0,0])
  plano2=ventana.add_subplot(plano[0,1])
  return(ventana)

graficar_varias_funciones()
plt.show()