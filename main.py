import numpy as np
import matplotlib.pyplot as plt

def funcion1(x):
  a = 0.2
  b = 0.4
  f = (np.sin(a*x) + np.cos(b*x))
  return (f)

def funcion2(x):
  a = 3
  f = 2**np.sin(a*x)
  return (f)

def funcion3(x):
  a = 8
  f = np.log(np.sin(a*x))
  return (f)

def funcion4(x):
  a = 3
  f = ((np.cos(a*x)**2)+1)/4
  return (f)

def configurar_grafica(plano, title, xlabel, ylabel ):
  plano.spines['top'].set_visible(False)
  plano.spines['right'].set_visible(False)
  plano.spines['bottom'].set_position('zero')
  plano.spines['left'].set_position('zero')
  plano.set_title(label = title, color = 'r', size = 8)
  plano.set_xlabel(xlabel=xlabel,labelpad=10)
  plano.set_ylabel(ylabel=ylabel, labelpad=10)

def graficar_funciones():
  ventana=plt.figure()
  plano=ventana.add_gridspec (2,2)
  plano1=ventana.add_subplot(plano[0,0])
  plano2=ventana.add_subplot(plano[0,1])
  plano3=ventana.add_subplot(plano[1,0])
  plano4=ventana.add_subplot(plano[1,1])

  configurar_grafica(plano1, 'Funciones Trigonometricas', 'Angulo Radianes', 'F(x) = sin(a*x) + cos(b* x)')
  configurar_grafica(plano2, 'Funciones Trigonometricas', 'Angulo Radianes', 'F(x) = 2**sin(a*x)')
  configurar_grafica(plano3, 'Funciones Trigonometricas', 'Angulo Radianes', 'F(x)=ln(sin(a*x))')
  configurar_grafica(plano4, 'Funciones Trigonometricas', 'Angulo Radianes', 'F(x)=( cos2(a*x)+1)/4')
  
  x1=np.linspace(0 ,2*np.pi,100)
  y1=funcion1(x1)

  x2=np.linspace(0 ,2*np.pi,100)
  y2=funcion2(x2)

  x3=np.linspace(0 ,2*np.pi,100)
  y3=funcion3(x3)

  x4=np.linspace(0 ,2*np.pi,100)
  y4=funcion4(x4)

  plano1.plot(x1,y1)
  plano1.set_yticks(np.arange(0, max(x1), 5))
  plano1.set_yticks(np.arange(0, max(y1), 5))
  plano2.plot(x2,y2)
  plano2.set_yticks(np.arange(0, max(x2), 5))
  plano1.set_yticks(np.arange(0, max(y2), 5))
  plano3.plot(x3,y3)
  plano3.set_yticks(np.arange(0, max(x3), 5))
  plano1.set_yticks(np.arange(0, max(y3), 5))
  plano4.plot(x4,y4)
  plano4.set_yticks(np.arange(0, max(x4), 5))
  plano1.set_yticks(np.arange(0, max(y4), 5))
  return(ventana)



graficar_funciones()
plt.show()