
#Ejemplo 1 crear una lista de numeros e imprimir el contenido

numeros=[4,6,2,89,78]
print(numeros)

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palabras=["angelin","jarra","lobo","sol"]
palabras_buscar=input("Ingrese una palabra a buscar: ")

if palabras_buscar in palabras:
    print(f"La palabra '{palabras_buscar}' se encuentra en la lista.")
else:
    print(f"La palabra '{palabras_buscar}' no se encuentra en la lista.")

#Ejemplo 2.1 buscar una palabra en la lista de palabras 
encontro=False
for i in palabras:
    if i==palabras_buscar:
       encontro=True
if encontro:
    print(f"La palabra '{palabras_buscar}' se encuentra en la lista.")

#Ejemplo 3 Añadir  elementos a la lista

numeros.append(13)
print(numeros)

palabras.append("manzana")
print(palabras)

#Ejemplo 4 crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[["pancho","618-123-4567"],["martina","618-987-6541"],["valeria","618-546-2310"]]