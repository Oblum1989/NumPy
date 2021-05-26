
import numpy as np
import matplotlib.pyplot as plt


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
    

#casos de prueba
grafica_ejercicio_1(-3.14,3.14,100,0.1,1)
plt.show()

def Posicion(a,xo,vo,t):
    y=xo+vo+t+((a*t**2)/2)
    return(y)


def grafica_ejercicio_2_posicion(j,k,n,a,xo,vo,num):
    ventana=plt.figure(num)
    plano=ventana.gca() 
    t=np.linspace(j,k,n)
    y=Posicion(a,xo,vo,t)
    plano.plot(t,y,'-.c',label='x(t)=xo+vo*t+((a*t**2)/2)')
    plano.legend(loc=2)
    plano.set_title(label='Posicion del objeto', color='b', size=10)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.set_xlabel(xlabel='Tiempo(s)',labelpad=10)
    plano.set_ylabel(ylabel='Posicion(m)',labelpad=40)
    plano.set_xticks([0,0.5,1])
    return(ventana)

#casos de prueba
grafica_ejercicio_2_posicion(0,1,10,7,35,0.8,1)
plt.show()

def Velocidad(a,vo,t):
    y=vo+a*t
    return(y)

def grafica_ejercicio_2_velocidad(j,k,n,a,vo,num):
    ventana=plt.figure(num)
    plano=ventana.gca() 
    t=np.linspace(j,k,n)
    y=Velocidad(a,vo,t)
    plano.plot(t,y,'-y',label='y=vo+a*t')
    plano.legend(loc=2)
    plano.set_title(label='Velocidad del objeto', color='g', size=10)
    plano.spines['top'].set_visible(False)
    plano.spines['right'].set_visible(False)
    plano.set_xlabel(xlabel='Tiempo(s)',labelpad=10)
    plano.set_ylabel(ylabel='Velocidad(m)',labelpad=40)
    plano.set_xticks([0,0.5,1])
    return(ventana)

#casos de prueba
grafica_ejercicio_2_velocidad(0,1,10,0.8,15,1)
plt.show()
