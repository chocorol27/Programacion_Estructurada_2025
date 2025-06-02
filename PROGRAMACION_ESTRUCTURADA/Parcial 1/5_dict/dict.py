"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("clear")
# ----------------------------
# Crear un diccionario
# ----------------------------
mi_dict = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario creado:", mi_dict)

# ----------------------------
# Acceder a un valor
# ----------------------------
print("Nombre:", mi_dict["nombre"])  # Output: Ana

# ----------------------------
# Usar get() para acceder de forma segura
# ----------------------------
print("Edad:", mi_dict.get("edad"))  # Output: 30
print("País:", mi_dict.get("pais", "No disponible"))  # Valor por defecto si no existe la clave

# ----------------------------
# Agregar o actualizar un valor
# ----------------------------
mi_dict["pais"] = "España"
mi_dict["edad"] = 31
print("Después de agregar/actualizar:", mi_dict)

# ----------------------------
# Eliminar un elemento con del
# ----------------------------
del mi_dict["ciudad"]
print("Después de eliminar 'ciudad':", mi_dict)

# ----------------------------
# Eliminar con pop()
# ----------------------------
valor = mi_dict.pop("pais")
print("Se eliminó 'pais':", valor)
print("Diccionario después de pop():", mi_dict)

# ----------------------------
# Claves, valores y pares (items)
# ----------------------------
print("Claves:", mi_dict.keys())     # dict_keys(['nombre', 'edad'])
print("Valores:", mi_dict.values()) # dict_values(['Ana', 31])
print("Items:", mi_dict.items())    # dict_items([('nombre', 'Ana'), ('edad', 31)])

# ----------------------------
# Recorrer un diccionario
# ----------------------------
for clave, valor in mi_dict.items():
    print(f"{clave}: {valor}")

# ----------------------------
# Comprobar si una clave existe
# ----------------------------
print("¿'edad' está en el dict?", "edad" in mi_dict)    # True
print("¿'ciudad' está en el dict?", "ciudad" in mi_dict)  # False

# ----------------------------
# Diccionarios anidados
# ----------------------------
usuarios = {
    "user1": {"nombre": "Ana", "edad": 30},
    "user2": {"nombre": "Luis", "edad": 25}
}
print("Usuario 1:", usuarios["user1"]["nombre"])  # Ana

# ----------------------------
# Crear un diccionario con dict()
# ----------------------------
otro_dict = dict(nombre="Carlos", edad=40)
print("Otro diccionario:", otro_dict)


