import mysql.connector
from mysql.connector import Error


def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprime tecla")   

def menu_principal():
    print("\n\t\t\t.::: Sistema de Gestión de Agenda de Contactos :::.\n\n\t\t\t\t\t\t1️⃣ Agregar contacto\n\t\t\t\t\t\t2️⃣ Mostrar todos los contactos\n\t\t\t\t\t\t3️⃣ Buscar contacto por nombre\n\t\t\t\t\t\t4️⃣ Borrar contacto\n\t\t\t\t\t\t3️5 Modificar contacto por nombre\n\t\t\t\t\t\t36. SALIR")
    opcion=input("\n\t\t\t 👉 Elige una opción (1-4): ").upper().strip()
    return opcion


def conectar():
    try:
        conexion=mysql.connector.connect(
             host="127.0.0.1",
             user="root",
             password="",
             database="bd_agenda"
         )
        return conexion
    except Error as e:
         print(f"El error que se presenta es: {e}")
         return None


def agregar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        print("Agregar contactos")
        nombre=input("Nombre: ").upper().strip()
        #sql="select * from agenda where nombre=%s"
        #val=(nombre,)
        #cursor.execute(sql,val)
        if nombre in agenda:
            print("Este contacto ya existe")
            
        else:
            tel=input("Telefono: ").strip()
            email=input("E-mail: ").lower().strip()
            agenda[nombre]=[tel,email]
            cursor=conexionBD.cursor()
            sql="insert into agenda (nombre, telefono, email) values (%s, %s, %s)"
            val=(nombre,tel,email)
            cursor.execute(sql,val)
            conexionBD.commit()
            print("Accion Realizada con éxito")
                     

def mostrar_contactos(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        print("Mostrar Contactos")
        if not agenda:
            print("No hay contactos")
        else:
            sql="select * from agenda"
            cursor.execute(sql)
            registros=cursor.fetchall()
            print("\n\t .:: Mostrar Contactos ::.\n")
            if registros:
                print(f"{'Nombre':<15} {'Telefono':<15} {'Email':<10}")
                print(f"-"*60)
                for fila in registros: #trae todo lo de los diccionarios, propia de ellos
                    print(f"{fila[1]:<15} {fila[2]:<15} {fila[3]:<10}")    
                print(f"-"*60)

# for fila in registros:
#           print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
#         print(f"-"*80) 


def buscar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        print("Mostrar contactos")
        if not agenda:
            print("No hay contactos a mostrar")

        else:
            nombre=input("Ingresa el nombre a buscar: ").upper().strip()
            cursor=conexionBD.cursor()
            if nombre in agenda:
                sql="select * from agenda where nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                registros=cursor.fetchall()
                if registros:
            # for nombres,datos in agenda.items():
            # print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}") 
                    print(f"{'Nombre':<15} {'Telefono':<15} {'Email':<10}")
                    print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")#accede al diccionario, se trae los valores pero en la posicion que quiera
                else: 
                    print("Contacto no existe")

def borrar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        print("Borrar contactos")
        if not agenda:
            print("No hay contactos a borrar")

        else:
            nombre=input("Ingresa el nombre a borrar: ").upper().strip()
            cursor=conexionBD.cursor()
            if nombre in agenda:
                sql="select * from agenda where nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                registros=cursor.fetchall()
                if registros:
                    yes=input("Deseas eliminar el contacto (Si/No): ").lower().strip()
                    if yes=="si":
                        sql="delete from agenda where nombre=%s"
                        val=(nombre,)
                        cursor.execute(sql,val)
                        conexionBD.commit()
            # for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
                    # agenda.pop(nombre)    
                        print("Accion realizada con exito")
                    else: 
                        print("No existe ese contacto")   
                               
                         
def modificar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        print("Modificar contactos")
        if not agenda:
            print("No hay contactos a modificar")

        else:
            nombre=input("Ingresa el nombre a modificar: ").upper().strip()
            cursor=conexionBD.cursor()
            if nombre in agenda:
                sql="select * from agenda where nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                registros=cursor.fetchall()
                if registros:
                    print(f"\n\tMostrar los contactos")
                    print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<15}")
                    print(f"-"*60)
                    for fila in registros:
                        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                        print(f"-"*80) 
                        resp=input("Deseas modificar los valores (Si/No): ").lower().strip()
                        if resp=="si":
                            nuevonombre=input("Ingresa el nuevo nombre: ").upper().strip()
                            tele=input("Ingresa el nuevo telefono: ").upper().strip()
                            mail=input("Ingresa el nuevo mail: ").upper().strip()
                            sql="update agenda set nombre = %s, telefono = %s, email = %s where nombre = %s"
                            val=(nuevonombre,tele,mail,nombre)
                            cursor.execute(sql,val)
                            conexionBD.commit()
                            print("Accion realizada con exito")
                       
                        else:
                            print("Este contacto no existe :()")    
                       