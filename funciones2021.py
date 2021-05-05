# comentarios en linea

"""
Comentarios enre varias lineas
sssss
sssss
sssss

"""

#Tipos de datos

# Enteros (int) 10 , 23, -5
# Flotantes (float) 3.6, 7.0
# String (str)  "casa", 'carro', '1234'
# Booleanos (bool)  True, False
# listas (list) [2,3,4,7,8,9]

#Asignacion: Darle un valor a una variable.
# Variable: espacio en memoria, guarda un dato.

w=10
x=4.5
y='casa'
z=True
#print(type(y))


######## FUNCIONNCIONES######

"""
* Autor: Estudiantes Programacion
**************
area_triangulo
**************
* Calcula el area de un triangulo a partir de su base y su altura.
*Parametros:
    base(int), base del triangulo (entero positivo)
    altura(int), altura del triangulo (entero positivo)
* Retorna:
    area(float), area del triangulo
* Casos de pruebas:
    area_triangulo(3,5) retorna 7.5
    area_triangulo(10,5) retorna 25.0
    area_triangulo(2,7) retorna 7.0
"""

def area_triangulo(base:int,altura:int)->float:
    area:float
    area=(base*altura)/2
    return(area)

#Casos prueba
"""
x=area_triangulo(3,5)
print(x)
x=area_triangulo(10,5)
print(x)
x=area_triangulo(2,7)
print(x)
"""



"""
* Autor: Estudiantes Programacion
**************
gravedad
**************
* Calcula el valor de la gravedad experimental.
*Parametros:
    tiempo(float), tiempo (flotante positivo)
    altura(float), altura de caida del cuerpo (flotante positivo)
* Retorna:
    g(float), el valor de la gravedad
* Casos de pruebas:
    gravedad(1.0,4.9) retorna 9.8
    gravedad(1.5,11.0) retorna 9.78
    gravedad(2.5,30.6) retorna 9.78
"""    
def gravedad(tiempo:float,altura:float)->float:
    g:float
    g=(2*altura)/(tiempo**2)
    return(g)

#Casos prueba
"""
x=gravedad(1.0,4.9)
print(x)
x=gravedad(1.5,11.0)
print(round(x,2)) #round(x,2) redondea a 2 decimales
x=gravedad(2.5,30.6)
print(round(x,2))
"""


#########  ESTRUCTURAS DE SELECCIÓN  ########

"""
* Autor: Estudiantes Programacion
**************
valor_absoluto
**************
* Calcula el valor absoluto de un numero
*Parametros:
    num(float), un numero 
* Retorna:
    r(float), el valor absoluto
* Casos de pruebas:
    valor_absoluto(-5.0) retorna 5.0
    valor_absoluto(15.0) retorna 15.0
    valor_absoluto(-40.7)retorna 40.7
"""  

def valor_absoluto(num:float)->float:
    r:float
    if (num<0):
        r=-num
    else:
        r=num
    return(r)
#Casos de prueba
"""
print(valor_absoluto(-5.0))
print(valor_absoluto(15.0))
"""
# funcion abs(num)
#print(abs(-40))

"""
* Autor: Estudiantes Programacion
**************
valor_absoluto
**************
* Calcula el valor absoluto de un numero
*Parametros:
    num(float), un numero 
* Retorna:
    r(float), el valor absoluto
* Casos de pruebas:
    valor_absoluto(-5.0) retorna 5.0
    valor_absoluto(15.0) retorna 15.0
    valor_absoluto(-40.7)retorna 40.7
"""  

def funcion_real (x:int)->int:
    fx:int
    if(x<-5):
        fx=x
    elif(-5<=x<=5):
        fx=x+3
    else:
        fx=(x**2)-2
    return(fx)
"""
#casos prueba
print(funcion_real(-7))
print(funcion_real(3))
print(funcion_real(6))
"""
# sueldo 100000
# v_extra = 100000/40 =2500
#h_extras =42-40 = 2
#valor_total_extras= 2500*2 = 5000
#recargo=5000*0.3= 1500
#salario = 100000+5000+1500 =106500

"""
* Autor: Estudiantes Programacion
**************
salario_empleado
**************
* Calcula el salario de un empleado.
*Parametros:
    horas(int), horas trabajadas a la semana( >=40 horas semana)
    sueldo(int), sueldo semanal
* Retorna:
    salario(float), salario total del empleado (sueldo mas comisiones)
* Casos de pruebas:
    salario_empleado(42,100000) retorna 106500.0
    salario_empleado(42,100000) retorna 100000.0
"""  


def salario_empleado(horas:int, sueldo:int)->float:
    v_extra:int= sueldo/40 # valor de la hora
    h_extras:int=horas-40 # total de horas extras 5
    if(h_extras>0):
        valor_total_extras:int=v_extra*h_extras # valor total horas extras
        recargo:float=(valor_total_extras)*0.3
        salario:float= sueldo+valor_total_extras+recargo # salario
    else:
        salario=sueldo
    return(salario)

"""
#Casos de prueba
print(salario_empleado(42,100000))
print(salario_empleado(40,100000))
"""
#tb = 500
#consumo = 0 -70
#consumo = 71 -170 cobro adiconal es de (50*100) = 5000  costo total =5500
#consumo = 171- 320 cobro adiconal es de (25*150) = 3750  costo total =9250
#consumo = >=321 cobro adiconal es de (15*x)


"""
* Autor: Estudiantes Programacion
**************
factura_gas
**************
* Calcula el valor de la factura de gas.
*Parametros:
   linicial(int), lectura inicial en metros cubicos
   lfinal(int), lectura final en metros cubicos
* Retorna:
    total_factura(int), costo total de la factura
* Casos de pruebas:
    factura_gas(0,70) retorna 500
    factura_gas(0,170) retorna 5500
    factura_gas(0,320) retorna 9250
    factura_gas(0,321) retorna 9265
"""  

def factura_gas(linicial:int,lfinal:int)->int:
    consumo:int=lfinal-linicial # consumo del mes en metros cubicos
    tb:int=500 # tarifa basica
    if(consumo<=70):
        total_factura:int=tb
    elif(70<consumo<=170):
        total_factura:int=tb+(consumo-70)*50  # 5500
    elif(170<consumo<=320):
        total_factura:int=5500+(consumo-170)*25  #9250
    else:
        total_factura:int=9250+(consumo-320)*15  #9250
        
        
    return(total_factura)
"""     
#Casos de prueba
print(factura_gas(0,70))
print(factura_gas(0,170))
print(factura_gas(0,320))
print(factura_gas(0,321))

"""
"""
* Autor: Estudiantes Programacion
**************
cafe_internet
**************
* Calcula el valor a pagar de un usuario a apartir de los minutos consumidos en un cafe internet.
*Parametros:
   minutos(int), minutos consumidos
* Retorna:
    total_factura(int), costo total de la factura del servicio de internet
* Casos de pruebas:
    cafe_internet(10) retorna 500
    cafe_internet(20) retorna 1000
    cafe_internet(40) retorna 1400
    cafe_internet(620) retorna 1440
""" 

def cafe_internet(minutos:int)->int:
    total_factura:int
    if(minutos<=15):
        total_factura=500
    elif(15<minutos<=30):
        total_factura=1000
    elif(30<minutos<=60):
        total_factura=1400
    else:
        total_factura=1400+(minutos-60)*20
    return(total_factura)
"""
# Casos de prueba
print(cafe_internet(10))
print(cafe_internet(20))
print(cafe_internet(40))
print(cafe_internet(62))
"""
"""
* Autor: Estudiantes Programacion
**************
factura_agua
**************
* Calcula el valor a pagar de la factura de agua apartir del estrato y el consumo.
*Parametros:
   estrato(int), estrato del usuario
   consumo(int), consumo del usuario
* Retorna:
    total_factura(int), costo total de la factura del servicio de agua.
* Casos de pruebas:
    factura_agua(1,9)) retorna 5000
    factura_agua(1,12) retorna 6600
    factura_agua(2,20) retorna 10000
    factura_agua(2,30) retorna 14000
    factura_agua(3,32)) retorna 15000
    factura_agua(3,37) retorna 16600
    factura_agua(4,39) retorna 20000
    factura_agua(4,42) retorna 21600
"""



def factura_agua(estrato:int,consumo:int)->int:
    total_factura:int
    t_basica:int
    """
    if(estrato==1):
        t_basica=5000
        if(consumo<=10):
            total_factura= t_basica
        else:
            total_factura= t_basica+(consumo-10)*800
    """
    if(estrato==1 and consumo<=10):
        total_factura=5000
    elif(estrato==1 and consumo>10):
        total_factura= 5000+(consumo-10)*800
    
    
    elif(estrato==2):
        t_basica=10000
        if(consumo<=25):
            total_factura= t_basica
        else:
            total_factura= t_basica+(consumo-25)*800
    elif(estrato==3):
        t_basica=15000
        if(consumo<=35):
            total_factura= t_basica
        else:
            total_factura= t_basica+(consumo-35)*800
    elif(estrato==4):
        t_basica=20000
        if(consumo<=40):
            total_factura= t_basica
        else:
            total_factura= t_basica+(consumo-40)*800
            
    return (total_factura)
"""
#casos de prueba
print(factura_agua(1,9))
print(factura_agua(1,12))
print(factura_agua(2,20)) # 10000
print(factura_agua(2,30)) # 10000 + 4000 = 14000
print(factura_agua(3,32)) # 
print(factura_agua(3,37)) #
print(factura_agua(4,39)) # 
print(factura_agua(4,42)) # 
"""   
# codigo  1 2 345
# d1 = carrera (1 2 3 )  valor base matricula 
# d2 = jornada (1 2) recargo (1-> 5%, 2->10% )
# d3 =  descuento (par -> 20% , impor -> 10%)
# vtm = valor base matricula + recargo -descuento


"""
* Autor: Estudiantes Programacion
**************
matricula_estudiante
**************
* Calcula el valor a pagar de la matricula de un estudiante a partir de la carrera, jornada y descuento (par, impar).
*Parametros:
   codigo(int), codigo del estudidiante (5 digitos)
* Retorna:
    vtm(float), valor total de la matricula.
* Casos de pruebas:
    matricula_estudiante(11230)) retorna 255000.0
    matricula_estudiante(11331))retorna 285000.0
    matricula_estudiante(12244)) retorna 270000.0
    matricula_estudiante(12111))retorna 300000.0
    matricula_estudiante(21230)) retorna 127500.0
    matricula_estudiante(21123)) retorna 142500.0
    matricula_estudiante(22232)) retorna 135000.0
    matricula_estudiante(22133)) retorna 150000.0
    matricula_estudiante(31232)) retorna 85000.0
    matricula_estudiante(31133)) retorna 950000.0
    matricula_estudiante(32250)) retorna 90000.0
    matricula_estudiante(32135)) retorna 100000.0
"""
def matricula_estudiante(codigo:int)->float:
    d1:int=(codigo//10000) # accedo el digito 1
    d2:int=(codigo%10000)//1000
    d3:int=codigo%1000
    v_base:int
    recargo:float
    descuento:float
    vtm:float
    
    if(d1==1 and d2==1):
        v_base=300000   # 300000
        recargo=v_base*0.05 # 15000
        if(d3%2==0):
            descuento=v_base*0.2 # 60000
        else:
             descuento=v_base*0.1
    elif(d1==1 and d2==2):
        v_base=300000
        recargo=v_base*0.1 # 30000
        if(d3%2==0):
            descuento=v_base*0.2 # 60000
        else:
             descuento=v_base*0.1
    elif(d1==2 and d2==1):
        v_base=150000
        recargo=v_base*0.05 #7500
        if(d3%2==0):
            descuento=v_base*0.2 # 30000
        else:
             descuento=v_base*0.1 # 15000
    elif(d1==2 and d2==2):
        v_base=150000
        recargo=v_base*0.1 # 15000
        if(d3%2==0):
            descuento=v_base*0.2 # 30000
        else:
             descuento=v_base*0.1 # 15000
    elif(d1==3 and d2==1):
        v_base=100000
        recargo=v_base*0.05 #5000
        if(d3%2==0):
            descuento=v_base*0.2 # 20000
        else:
             descuento=v_base*0.1 # 10000   
    elif(d1==3 and d2==2):
        v_base=100000
        recargo=v_base*0.1 # 10000
        if(d3%2==0):
            descuento=v_base*0.2 # 20000
        else:
             descuento=v_base*0.1 # 10000               
    vtm=v_base+recargo-descuento
         
    return(vtm) # 300000+15000-60000 = 255000

#Caso de prueba
#print(matricula_estudiante(11230)) #255000.0
#print(matricula_estudiante(11331))#285000.0
#print(matricula_estudiante(12244)) #270000.0
#print(matricula_estudiante(12111)) #300000.0
#print(matricula_estudiante(21230)) #127500.0
#print(matricula_estudiante(21123)) #142500.0
#print(matricula_estudiante(22232)) #135000.0
#print(matricula_estudiante(22133)) #150000.0
#print(matricula_estudiante(31232)) #85000.0
#print(matricula_estudiante(31133)) #950000.0
#print(matricula_estudiante(32250)) #90000.0
#print(matricula_estudiante(32135)) #100000.0

"""
* Autor: Estudiantes Programacion
**************
factura_celular
**************
* Calcula el valor a pagar de la factura de celular apartir de el tipo de plan, minutos y mensajes consumidos.
*Parametros:
    plan(str), el tipo de plan.
    minutos(int), minutos consumidos
    mensajes(int), mensajes consumidos
* Retorna:
    costo_factura(int), costo total de la factura de celular.
        
* Casos de pruebas:
    #print(factura_celular('ideal',45,7)) retorna  80000
    #print(factura_celular('ideal',101,7)) retorna 80855
    #print(factura_celular('ideal',90,11)) retorna  80370
    #print(factura_celular('ideal',101,11)) retorna  81225
    #print(factura_celular('extension',120,15)) retorna  120000
    #print(factura_celular('extension',136,17)) retorna  120855
    #print(factura_celular('extension',120,21)) retorna  120370
    #print(factura_celular('extension',136,21)) retorna 121225       
    #print(factura_celular('familiar',400,25)) retorna 180000
    #print(factura_celular('familiar',426,25)) retorna 180855
    #print(factura_celular('familiar',421,31)) retorna 180370
    #print(factura_celular('familiar',426,31)) retorna  181225    


"""
def factura_celular(plan:str,minutos:int, mensajes:int)->int:
    c_basico:int
    costo_factura:int
    minutos_extras:int
    vminutos_extras:int=0
    vmensajes_extras:int=0
    if(plan=='ideal'):
        c_basico=80000
        if(minutos>100):
            vminutos_extras=(minutos-100)*855
        if(mensajes>10):
            vmensajes_extras=(mensajes-10)*370
            
    elif(plan=='extension'):
        c_basico=120000
        if(minutos>135):
            vminutos_extras=(minutos-135)*855
        if(mensajes>20):
            vmensajes_extras=(mensajes-20)*370
            
    elif(plan=='familiar'):
        c_basico=180000
        if(minutos>425):
            vminutos_extras=(minutos-425)*855
        if(mensajes>30):
            vmensajes_extras=(mensajes-30)*370
            
    costo_factura=c_basico+vminutos_extras+vmensajes_extras
    
    return(costo_factura)
#casos de prueba
#print(factura_celular('ideal',45,7)) # 80000
#print(factura_celular('ideal',101,7)) #80855
#print(factura_celular('ideal',90,11)) #80370
#print(factura_celular('ideal',101,11)) #81225

#print(factura_celular('extension',120,15)) # 120000
#print(factura_celular('extension',136,17)) #120855
#print(factura_celular('extension',120,21)) #120370
#print(factura_celular('extension',136,21)) #121225       
    
#print(factura_celular('familiar',400,25)) # 180000
#print(factura_celular('familiar',426,25)) #180855
#print(factura_celular('familiar',421,31)) #180370
#print(factura_celular('familiar',426,31)) #181225    

###### ESTRUCTURAS DE CONTROL REPETITIVAS ######


"""
* Autor: Estudiantes Programacion
**************
factorial
**************
* Calcula el factorial de un numero entero positivo.
*Parametros:
    num(int), un numero entero postivo
   
* Retorna:
    f(int), el factorial de num
        
* Casos de pruebas:
    factorial(0) retorna 1
    factorial(1) retorna 1
    factorial(4) retorna 24
    factorial(5) retorna 120

"""
# factorial 0 = 1
# factorial 1 = 1
# factorial 2 = 1*2 = 2
# factorial 3 = 1*2*3= 6
# factorial 4 = 1*2*3*4= 24
# factorial 5 = 1*2*3*4*5= 120


def factorial(num:int)->int: #5
    f:int=1
    while(num>1):#1
        f=f*num # 1*4=4*3=12*2=24
        num-=1

    return(f)
"""
#Casos de prueba
print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(5))      
"""

# 10**4 = 2*2*2*2

#Ejercicio para despues de semana santa

def potencia(b:int,e:int)->int:
    p:int=1
    while(e>0):
        p=p*b
        e-=1
    return(p)

#Casos de prueba
"""
print(potencia(2,3))
print(potencia(4,3))
print(potencia(4,3))
print(potencia(5,0))
"""
#print(pow(2,3)) #pow(base,exponente)
#print(pow(2,-3)) #pow(base,exponente)


def contar_digitos(num:int)->int: #543
    cont:int=0
    while(num>0):#543
        num=num//10 #543//10 = 54//10=5//10=0
        cont+=1 #3
    return(cont)
"""
#Casos de prueba
print(contar_digitos(765432))
print(contar_digitos(12345))
print(contar_digitos(987))
"""
# 6 dividir 1, 2, 3 4, 5 residuo es =0 sumando

###### Cooperacion entre fucniones #####

def suma_divisores_propios(num:int)->int:
    k:int=1
    suma:int=0
    while(k<num):
        if(num%k==0):
            suma=suma+k
        k+=1
    return(suma)
"""
#casos de prueba
print(suma_divisores_propios(9))
print(suma_divisores_propios(6))
print(suma_divisores_propios(10))
            
"""


def numero_perfecto(num:int)->bool:
    x:int=suma_divisores_propios(num)
    a:bool=False
    if(x==num and num!=0):
        a=True
    
    return(a)
"""
#caso Prueba
print(numero_perfecto(6))
print(numero_perfecto(7))
print(numero_perfecto(0))
"""

# 1er termino = 1 -> 
# 2do termino = 1 -> a
# 3er termino = 2 -> b
# 4to termino = 3
# 5to termino = 5
# 6to termino = 8
# 7to termino = 13

def fibonacci(num:int)->int:
    a:int=1
    b:int=1
    k:int=3
    f:int=1
    while(k<=num): #5   k 4
        f=a+b #2
        a=b
        b=f      
        k+=1
    return(f)
"""
#casos de prueba
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
"""

# funcion total_divisores -> cantidad de div del num
# 5 -> 1, 2,3,4,5  =0 cont +
# numero_primo -> True False

def total_divisores(num:int)->int:
    k:int=1
    cont:int=0
    while(k<=num):
        if(num%k==0):
            cont+=1 # almacenando la cantidad de divisores
        k+=1
    return(cont)
"""
#Casos de prueba
print(total_divisores(6)) #1 2 3 6 = 4
print(total_divisores(7)) #1 7 =2
print(total_divisores(12)) #1 2 3 4 6 12 = 5
"""           
    
def numero_primo(num:int)->bool:
    x:int=total_divisores(num)
    a:bool=False
    if(x==2):
        a=True

    return(a)
"""
#casos de prueba
print(numero_primo(2))
print(numero_primo(7))
print(numero_primo(12))
print(numero_primo(17))
print(numero_primo(1))
"""

def total_km(km:float,dias:float)->float: #cantidad de de km acumulados hasta el dias
    acumulado:float=km # 5
    k:int=2
    while(k<=dias):
        if(k%3==0):
            km=km/2
        else:
            km=(km*2)+10
        acumulado=acumulado+ km
        k+=1
    return(acumulado)
"""
#Casos de prueba
print(total_km(5.0,1.0))
print(total_km(5.0,2.0))
print(total_km(5.0,3.0))
print(total_km(5.0,5.0))
print(total_km(5.0,6.0))
print(total_km(5.0,7.0))
print(total_km(5.0,8.0))
print(total_km(5.0,9.0))
"""

# numeros amigos

#num1 = 220 --> hallar los suma de los div propios -> x
#num2 = 284 --> hallar los suma de los div propios-> y
# (x==num) and (y==num)


def numeros_amigos(num1:int,num2:int)->bool:
    x:int=suma_divisores_propios(num1)
    y:int=suma_divisores_propios(num2)
    a:bool=False
    
    if((x==num2) and (y==num1)):
        a=True
    return(a)

"""
#casos de prueba
print(numeros_amigos(220,284))
print(numeros_amigos(1184,1210))
print(numeros_amigos(20,15))
"""   

#narcicista
# numero_narcicista()
# contar_digitos()
# suma_potencias()
# 153 -> 3**(exponente) -> 5**(exponente) -> 1**(exponente) = suma

def suma_potencias(num:int)->int:
    exponente:int=contar_digitos(num)
    suma:int=0
    while(num>0): #0
        n=num%10 #1
        suma=suma+n**(exponente)
        num=num//10
        
    return(suma)

"""
#Casos de prueba
print(suma_potencias(153))# 27+125+1 =153
print(suma_potencias(15)) # 25 +1=26
print(suma_potencias(9784))#256+4096+2401+6561 = 13314
"""        
def numero_narcicista(num:int)->bool:
    x:int=suma_potencias(num)
    a:bool=False
    if(x==num):
        a=True
    return(a)
"""
#Casos prueba
print(numero_narcicista(153)) #True
print(numero_narcicista(15)) #False
print(numero_narcicista(345))#False
print(numero_narcicista(9474)) #True
"""
# Calcular el valor de pi mediante sumatorias

def potencia_2(e:int)->int:
    p:int=-1
    if((e%2)==0):
        p=1
       
    return(p)
"""
#caso de prueba
print( potencia_2(4))
print( potencia_2(3))
"""

def sumatoria_pi(num:int)->float:
    k:int=1
    suma:float=0
    while(k<=num):
        numerador:int=potencia_2(k+1)
        denominador:int=(2*k)-1
        suma=suma+(numerador/denominador)
        k+=1
    return(4*suma)


"""
#Casos de prueba
print(sumatoria_pi(50))
print(sumatoria_pi(500))
print(sumatoria_pi(1000))
print(sumatoria_pi(10000))
"""


# ++++++++ ARREGLOS UNIDIMENSIONALES+++++++

#listas
a=[2,3.5,'casa',4,7,[2,4,5]] #lista

# Arreglos unidimencionales

x=[2,4,6,7,9,2,3,5,7]
y=[3.5,5.9,7.3,9.8,3.2]
z=['casa','carro','+','s']

#print(len(z))
#print(x)
#x.append(56)
#x.insert(3,100)
#x.pop(5)
#del x[5]
#w=x[3:7]


P=list(range(11))
S=list(range(4,11))
T=list(range(4,11,3))
W=list(range(20,2,-3))
#print(W)


# estudiar los ejercicios hasta el ejemplo 5

# sumar los elementos de un arreglo

def sumar_arreglo(A:list)->int:
    n:int=len(A)
    suma:int=0
    k:int=0
    while(k<n):
        suma=suma+A[k]
        k+=1
    return(suma)

#caso de prueba

#A=[1,3,5,7,8,9,-5]
#print(sumar_arreglo(c))

def dato_menor(A:list)->int:
    n:int=len(A)
    mn:int=A[0] #10 menor
    k:int=1
    while(k<n):
        if(A[k]<mn):
            mn=A[k] #-5
        k+=1
    return(mn)



#caso de prueba
#A=[10,3,50,7,2,9,-5,-100]#
#print(dato_menor(A))

def dato_mayor(A:list)->int:
    n:int=len(A)
    my:int=A[0] #10 mayor
    k:int=1
    while(k<n):
        if(A[k]>my):
            my=A[k] #-5
        k+=1
    return(my)



#caso de prueba
#A=[10,3,50,7,2,9,-5,-100]#
#print(dato_mayor(A))


# [9,2,7,4,5,1]  --> [9,5,4,7,2,1]
#  0 1 2 3 4 5   n=6
# aux= 1
# A[0]=A[5]
# A[5]=aux
def arreglo_invertido(A:list)->list:
    n:int=len(A)
    k:int=0
    while(k<n):
        aux=A[k]
        A[k]=A[n-1]
        A[n-1]=aux
        k+=1
        n-=1
    return(A)
        
#Casos de prueba

A=[1,2,3,4,5,6]
B=[1,2,3,4,5,6,7]
#print(arreglo_invertido(A))
#print(arreglo_invertido(B))

# 367 ->>> 763
#   7  ---> suma
#   7*10+6 = 76
#   76*10+3 = 763
# x = 763%10 ---> 7
# suma= 0
# suma =x +(suma*10)  = 7+(0*10)=7
# suma= 6+(7*10)=76
# suma= 3+(76*10)=763

def invertir_numero(num:int)->int: #367
    suma:int=0
    while(num>0): #0
        x:int=num%10
        suma=x+(suma*10)
        num=num//10
    return(suma)

#casos de prueba
#print(invertir_numero(367))
#print(invertir_numero(974196))   
    
# A=[23,564,12345,7943]   -> B=[32,465,54321,3497]

def arreglo_espejo(A:list)->list:
    n:int=len(A)
    B:list=[]
    k:int=0
    while(k<n):
        m:int=invertir_numero(A[k])
        B.append(m)
        k+=1
    return(B)

#casos de prueba
#A=[23,564,12345,7943]
#print(arreglo_espejo(A))

def promedio_deportista(A:float)->float:
    cal_menor:float= dato_menor(A)
    cal_mayor:float= dato_mayor(A)
    suma:float= sumar_arreglo(A)
    promedio:float=(suma-cal_menor-cal_mayor)/8

    return(promedio)
    
#Casos de prueba

#A=[4.9,7.6,5.5,3.1,7.9,4.6,9.0,8.4,5.4,6.2]
#print(promedio_deportista(A))


def primo_perfecto(A:list)->tuple:
    n:int=len(A)
    k:int=0
    primo:list=[]
    perfecto:list=[]
    while(k<n):
        a:bool=numero_primo(A[k])
        if(a==True):
            primo.append(A[k])
        b:bool=numero_perfecto(A[k])
        if(b==True):
            perfecto.append(A[k])
        k+=1
    print(primo)
    print(perfecto)
    return(primo,perfecto)


#casos de prueba
#A=[2,40,25,7,40,28,17,45,6,0,4,5]
#print(primo_perfecto(A))        

# ARRGLOS BIDIMENSIONALES   #######
def matriz_como_cadena(M:list)->str:
    nf:str=len(M)
    nc=len(M[0])
    cadena:str= ''
    j:int=0
    while(j<nf):
        cadena = cadena + ''
        k:int=0
        while (k<nc):
            cadena = cadena +'{:>10s}'.format(str(M[j][k]))
            k+=1
        cadena = cadena + '\n'
        j+=1
    return (cadena)
# arreglo en dos diemensiones

M:list = [[2,5,6,9],[65,7,89,60],[87,34,23,10],[9,34,23,21],[9,8,2,11]]
#print(len(M)) # numero de filas
#print(len(M[0])) # numero de columnas

def suma_elementos_matriz(M:list)->int:
    nf:int=len(M)# cantidad filas
    nc:int=len(M[0])
    suma:int=0
    j:int=0
    while(j<nf):
        k:int=0
        while(k<nc):
            suma=suma+M[j][k]
            k+=1
        j+=1
    return(suma)
#Casos de prueba

M:list = [[2,5,6,9],[65,7,89,60],[87,34,23,10],[9,34,23,21],[9,8,2,11]]
#M:int=[[1,2,3],[4,5,6]]
#print(suma_elementos_matriz(M))


def suma_columna_matriz(M:list,col:int)->int:
    nf:int=len(M)
    suma:int=0
    j:int=0
    while(j<nf):
        suma=suma+M[j][col]
        j+=1
    return(suma)
#print(suma_columna_matriz(M,0))
#print(suma_columna_matriz(M,1))
def suma_fila_matriz(M:list,fila:int)->int:
    nc:int=len(M[0])
    suma:int=0
    k=int=0
    while(k<nc):
        suma=suma+M[fila][k]
        k+=1
    return(suma)
         
#Casos deprueba

#print(suma_fila_matriz(M,0))
#print(suma_fila_matriz(M,2))

def suma_diagonal_principal(M:list)->int:
    nf:int=len(M)
    suma:int=0
    j:int=0
    while(j<nf):
        suma=suma+M[j][j]
        j+=1
    return(suma)

#Casos de prueba
M:list=[[3,2,4],[3,5,6],[8,5,2]]
#print(suma_diagonal_principal(M))

def suma_diagonal_secundaria(M:list)->int:
    nf:int=len(M)
    suma:int=0
    j:int=0
    k:int=len(M[0])-1#2
    while(j<nf):
        suma=suma+M[j][k] #[2][0]
        j+=1
        k-=1
    return(suma)
#Casos de prueba
#print(suma_diagonal_secundaria(M))
#print(matriz_como_cadena(M))

# libreria random
import random as rd
# chr(num)--->generar un string mediante el codigo ascii
# A-Z ---->(65,90)
# a-z-----> (97,122)
# rd.randint(j,k)---> genera un num aleatorio entero entre en rango (j,k)
# rd.uniform(j,k)---> genera un num aleatorio flotante entre en rango (j,k)
# print(chr(rd.randint(97,122)))# genera una letra minus aleatoria
# print(chr(rd.randint(65,90)))# genera una letra mayus aleatoria
print(chr(rd.randint(65,90)))

#print(rd.randint(1,10))
#print(round(rd.uniform(-3.5,5.5),2))

def generar_matriz_enteros(nf:int,nc:int,desde:int,hasta:int)->list:
    M:list=[]
    j:int=0
    while(j<nf):
        A:list=[]
        k:int=0
        while(k<nc):
            A.append(rd.randint(desde,hasta))
            k+=1
        M.append(A)
        j+=1
    return(M)
    

#Casos de prueba
#C=generar_matriz_enteros(3,5,20,30)
#print(matriz_como_cadena(C))
































    
    























    
    

    
        
    
    
