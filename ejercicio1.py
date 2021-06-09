import numpy as np
import matplotlib.pyplot as plt


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

  plano1.plot(t,x1,'--c',label='Carga')
  plano1.legend(loc=2)
  plano1.set_xticks([0, limisuperior//2, limisuperior])
  plano1.set_yticks([0, max(x1)//2, max(x1)])

  plano2.plot(t,x2,'--r',label='Descarga')
  plano2.legend(loc=1)
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