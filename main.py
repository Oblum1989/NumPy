import numpy as np
import matplotlib.pyplot as plt
import ejercicio1 as eg


def funcion_potencia(i):
	p = 120 * i
	return (p)


print(np.arange(9, 15))


def graficar_potencia(i):
	ventana = plt.figure()
	plano = ventana.gca()
	x = np.arange(9, 15)
	y = funcion_potencia(i)
	plano.plot(x, y, 'h--c', label='P=V*I')
	plano.legend(loc=2)
	plano.set_title(label='Función Potencia', color='r', size=20)
	plano.set_xlabel(xlabel='Tiempo(h)', labelpad=10)
	plano.set_ylabel(ylabel='Potencia(w)', labelpad=10)

	return (ventana)


def informacion_potencia():
	print('-----------------Descripción-----------------')

	print('La potencia electrica esta definida por la siguiente formula.')
	print('+------------------------------+')
	print('| Potencia electrica           |')
	print('| P = V * I                    |')
	print('+------------------------------+')
	print('Donde:')
	print('P = Potencia.')
	print('V = Voltaje')
	print('I = Corriente')

	print('----------------Ingreso información--------------')

	print('Ingresa el valor de la corriente en en instante 9am')
	i1 = float(input('Digite el valor de la corriente: '))

	print('--------------Ingreso información----------------')

	print('Ingresa el valor de la corriente en en instante 10am')
	i2 = float(input('Digite el valor de la corriente: '))

	print('--------------Ingreso información----------------')

	print('Ingresa el valor de la corriente en en instante 11am')
	i3 = float(input('Digite el valor de la corriente: '))

	print('--------------Ingreso información----------------')

	print('Ingresa el valor de la corriente en en instante 12pm')
	i4 = float(input('Digite el valor de la corriente: '))

	print('--------------Ingreso información----------------')

	print('Ingresa el valor de la corriente en en instante 1pm')
	i5 = float(input('Digite el valor de la corriente: '))

	print('--------------Ingreso información----------------')

	print('Ingresa el valor de la corriente en en instante 2pm')
	i6 = float(input('Digite el valor de la corriente: '))

	i = np.array([i1, i2, i3, i4, i5, i6])
	graficar_potencia(i)
	plt.show()


def inicio():
	print('-----------------Calcular Potencia Electrica------------------')
	while True:
		print('Digite la opción que desee para continuar')
		print('0. Para salir')
		print('1. Para graficar potencia electrica con respecto al tiempo.')
		opcion = int(input('Opcion ===>: '))
		if (opcion == 0):
			print('Finalizó programa===>')
			break
		elif (opcion == 1):
			informacion_potencia()


eg.inicio()
