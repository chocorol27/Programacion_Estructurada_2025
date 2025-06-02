"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
import os
os.system("clear")
# ----------------------------
# Crear una tupla
# ----------------------------
mi_tupla = (1, 2, 3)
print("Tupla creada:", mi_tupla)

# ----------------------------
# Tupla con diferentes tipos de datos
# ----------------------------
tupla_mixta = (1, "hola", 3.14, True)
print("Tupla mixta:", tupla_mixta)

# ----------------------------
# Acceder a elementos
# ----------------------------
print("Primer elemento:", mi_tupla[0])   # Output: 1
print("Último elemento:", mi_tupla[-1])  # Output: 3

# ----------------------------
# Longitud de una tupla
# ----------------------------
print("Longitud:", len(mi_tupla))  # Output: 3

# ----------------------------
# Tupla de un solo elemento
# ----------------------------
tupla_1 = (5,)  # Ojo con la coma
print("Tupla de un elemento:", tupla_1)

# ----------------------------
# No se pueden modificar (inmutables)
# ----------------------------
# mi_tupla[0] = 10  # ❌ Esto da error: TypeError

# ----------------------------
# Recorrer una tupla
# ----------------------------
for elemento in mi_tupla:
    print("Elemento:", elemento)

# ----------------------------
# Comprobar si existe un valor
# ----------------------------
print("¿2 está en la tupla?", 2 in mi_tupla)  # True
print("¿10 está en la tupla?", 10 in mi_tupla)  # False

# ----------------------------
# Concatenar tuplas
# ----------------------------
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

# ----------------------------
# Repetir tuplas
# ----------------------------
tupla_repetida = tupla1 * 3
print("Tupla repetida:", tupla_repetida)  # (1, 2, 1, 2, 1, 2)

# ----------------------------
# Desempaquetado (unpacking)
# ----------------------------
persona = ("Ana", 30, "España")
nombre, edad, pais = persona
print("Nombre:", nombre)
print("Edad:", edad)
print("País:", pais)

# ----------------------------
# Usar tuplas como claves en diccionarios
# ----------------------------
coordenadas = {(10, 20): "Punto A", (30, 40): "Punto B"}
print("Valor en (10, 20):", coordenadas[(10, 20)])

# ----------------------------
# Tupla anidada
# ----------------------------
tupla_anidada = ((1, 2), (3, 4))
print("Elemento anidado:", tupla_anidada[1][0])  # Output: 3
