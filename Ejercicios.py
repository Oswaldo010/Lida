# Práctica 03: Calcular propina
# Cree un programa en Python 3 que le solicite al usuario dos números enteros, el primero es el costo total de la comida y el segundo es el porcentaje de propina que debe pagar, y luego calcule el valor de la propina.  El programa debe mostrar como resultado exclusivamente  el valor de la propina aproximada a dos cifras decimales, no debe contener letras ni enunciados que lo acompañen.
# Por ejemplo, si el usuario ingresa 100000 como valor de la comida y 20 como porcentaje de propina, el programa debe mostrar:
# 20000
# Elabore su programa en un archivo de Python (formato *.py). Si omite la extensión le aparecerá un error de compilación.
# Solución
# Nombre del archivo: propina.py
x=int(input())
y=int(input())
z=y/100
w=x*z
print(w)

# Práctica 04: Promedio de notas de un trabajo
# Cree un programa en Python 3 que le solicite al usuario cinco valores reales que corresponden a las notas de una entrega de un trabajo.
# Se deben guardar las cinco notas en una lista en el respectivo orden de entrada y se debe calcular el promedio de las cinco notas (aproximado a dos cifras decimales) y agregarlo al final de la lista. El programa debe mostrar como resultado exclusivamente la lista, no debe contener letras ni enunciados que lo acompañen.
# Elabore su programa en un archivo de Python (formato *.py). Si omite la extensión le aparecerá un error de compilación.
# Solución
# Nombre del archivo: promedionotas.py
x=float(input())
y=float(input())
z=float(input())
w=float(input())
f=float(input())
lista=[x,y,z,w,f]
promedio=round(((x+y+z+w+f)/5),2)
p1=[promedio]
print(lista+p1)

# Práctica 05: Transformar una lista
# Cree un programa en Python 3 que le solicite al usuario ingresar tres valores, luego agregue los tres valores a una lista, después concatene tres veces la misma lista y finalmente muestre la lista de la posición dos (inclusive) en adelante por pantalla. 
# El programa debe mostrar como resultado exclusivamente la lista, no debe contener letras ni enunciados que lo acompañen.
# Por ejemplo, si el usuario ingresa los valores 7, 5 y 4 el programa debe mostrar:
# [4,7, 5,4, 7,5, 4]
# Elabore su programa en un archivo de Python (formato *.py). Si omite la extensión le aparecerá un error de compilación.
# Solución
# Nombre del archivo: transformarlista.py
x=int(input())
y=int(input())
z=int(input())
w=[x,y,z]
f=w*3
print(f)

# Práctica 06: Distancia entre dos puntos
# Cree un programa en Python 3 que le solicite al usuario las coordenadas (x,y) de dos puntos (X del primer punto = input1, Y  del primer punto = input2, X del segundo punto =input3, Y del segundo punto = input4, y luego calcule la distancia entre los dos puntos  El programa debe mostrar como resultado exclusivamente la distancia aproximado a dos cifras decimales, no debe contener letras ni enunciados que lo acompañen.
# Nota: recuerde que la raíz cuadrada es igual a elevar el número a la 0.5
# Por ejemplo, si el usuario ingresa como coordenadas del primer punto (7, 5) y como coordenadas del segundo punto (4, 1),  el programa debe mostrar:
# 5
# Elabore su programa en un archivo de Python (formato *.py). Si omite la extensión le aparecerá un error de compilación.
# Solución
# Nombre del archivo: distanciaentredospuntos.py

x=float(input())
y=float(input())
z=float(input())
w=float(input())
distancia=((((x-z)**2)+((y-w)**2))**(1/2))
f=round(distancia,2)
print(f)

