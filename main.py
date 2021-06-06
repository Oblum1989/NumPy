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

def funcion_carga_condensador(t, u, r, c):
  v = u * ( 1 - np.e**(-t/(r*c)) )
  return(v)
def funcion_descarga_condensador(t, u, r, c):
  v = u * np.e**(-t/(r*c))
  return(v)

def configurar_grafica(plano, title, xlabel, ylabel ):
  plano.set_title(label = title, color = 'm', size = 10)
  plano.spines['top'].set_visible(False)
  plano.spines['right'].set_visible(False)
  plano.spines['bottom'].set_position('zero')
  plano.spines['left'].set_position('zero')
  plano.set_xlabel(xlabel=xlabel,labelpad=10)
  plano.set_ylabel(ylabel=ylabel, labelpad=10)

def graficar_carga_descarga_condensador(u1, r1, c1, u2, r2, c2):
  ventana=plt.figure()
  plano=ventana.add_gridspec (1,2)
  plano1=ventana.add_subplot(plano[0,0])
  plano2=ventana.add_subplot(plano[0,1])
  configurar_grafica(plano1, 'Carga Condensador', 'Tiempo (s)', 'Voltaje (v)')
  configurar_grafica(plano2, 'Descarga Condensador', 'Tiempo (s)', 'Voltaje (v)')
  liminferior=0
  limisuperior=int(input('Digite el tiempo en segundos: '))
  t=np.linspace(liminferior,limisuperior,100)

  x1 = funcion_carga_condensador(t, u1, r1, c1)
  x2 = funcion_descarga_condensador(t, u2, r2, c2)

  plano1.plot(t,x1,'.--c',label='carga')
  plano1.set_xticks([0, limisuperior//2, limisuperior])
  plano1.set_yticks([0, max(x1)//2, max(x1)])

  plano2.plot(t,x2,'.--c',label='descarga')
  plano2.set_xticks([0, limisuperior//2, limisuperior])
  plano2.set_yticks([0, max(x2)//2, max(x2)])
  
  return(ventana)

def informacion_carga_descarga():
  print('-----------------Descripción-----------------')
  
  print('Las siguientes expresiones representan la carga y descarga de un condensador en determinado tiempo.')
  print('+------------------------------+')
  print('| Carga de un condensador      |')
  print('| v(t) = U * (1 - e**(-t/R*C)) |')
  print('+------------------------------+')
  print('+------------------------------+')
  print('| Descarga de un condensador   |')
  print('| v(t) = U * e**(-t/R*C)       |')
  print('+------------------------------+')
  print('Donde:')
  print('v(t) = Diferencia de potencial en determinado tiempo.')
  print('U = Voltaje de la fuente')
  print('R = Valor de la resistencia')
  print('C = Valor del condensador')
  
  print('----------------Ingreso información--------------')
  
  print('Ingresa los valores para la carga del condensador')
  u1=float(input('Digite el valor de voltaje de la fuente: '))
  r1=float(input('Digite el valor de la resistencia: '))
  c1=float(input('Digite el valor del condensador: '))
  
  print('--------------Ingreso información----------------')
  
  print('Ingresa los valores para la descarga del condensador')
  u2=float(input('Digite el valor de voltaje de la fuente: '))
  r2=float(input('Digite el valor de la resistencia: '))
  c2=float(input('Digite el valor del condensador: '))

  graficar_carga_descarga_condensador(u1, r1, c1, u2, r2, c2)
  plt.show()


def inicio():
  print('-----------------Carga y Descarga de un Condensador------------------')
  while True:
    print('Digite la opcion que desee para continuar')
    print('0. Para salir')
    print('1. Para graficar carga del condensador y descarga del condensador en un instante t.')
    opcion=int(input('Opcion ===>: '))
    if(opcion == 0):
      print('Finalizó programa===>')
      break
    elif(opcion == 1):
      informacion_carga_descarga()

inicio()