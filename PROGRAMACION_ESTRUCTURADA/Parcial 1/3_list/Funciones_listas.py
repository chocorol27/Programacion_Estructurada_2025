
""""
List(array)
son collecioes o conjunto de datos/valores bajo un mismo nombre,para acceder a los valores se
hace con un indice numerico
Nota:sus valores si con modificables
La lista es una coleccion ordenada y modificable
Permite miembros duplicados.
"""
import os
os.system("clr")
#Funciones mas comunes las listas
paises=["Mexico","España","Brasil","Canada"]

numeros=[23,45,8,24]

varios=["Hola",123.7,True]

print(paises)
print(numeros)
print(varios)

#primera forma
for i in paises:
 print(i)

#Segunda forma
for i in range(0,len(paises)):
    print   (paises[i])

#Orden de elementos de una lista
paises.sort()
print(paises)
print(numeros)

#darle la vuelta a una lista
paises.reverse()
print(paises)

varios.reverse()
print(varios)

#Agregar un elemneto a una lista
#primera forma
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")

#Eliminar un elemento de una lista
#primer forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")
print (paises)
#Buscar un elemento dentro de la lista
print(paises)
"brasil" in paises
print("Brasil" in paises)

#contar el numero de veces que aparece un elemento dentro de una lista
cuantos=numeros.count(23)
print(cuantos)

#conoce la posiscion o indice en el que se encuentra un elemento en de la lista
print(paises)
posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posicion{posicion}")

#unir el contenido de una lista dentron de otra lista

print(numeros)
numeros2=[100,200]
print(numeros2)

#Crear a partir de las listas de numeros 1 y 2 un resultado un resultante y mostrar en contenido ordenado descendemente

numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)  

numeros.reverse()
print(numeros)