import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\u2B50 Gestión de Calificaciones \u2B50\n\n\t1\uFE0F\u20E3\tAgregar\n\t2\uFE0F\u20E3\tMostrar\n\t3\uFE0F\u20E3\tCalcular Promedios\n\t4\uFE0F\u20E3\tSalir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion: ").upper()
    return opcion

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def agregar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t\t\U0001F4BE Agregar calificaciones \U0001F4BE")
        nombre=input("\t\t\U0001F464 Ingrese el nombre del alumnos: ").upper().strip()
        calificaciones=[]
        for i in range(1,4):
            continua=True
            while continua:
                try:
                    #calificaciones.append(float(input(f"Calificacion #{i}: ")))
                    cal=float(input(f"\t\t\U0001F4BE Calificacion #{i}: "))
                    if cal>=0 and cal<=10:
                        calificaciones.append(cal)
                        continua=False
                    else:
                        print("\t\t\t\u274C Ingresa una calificacion valida del 0 al 10")
                except ValueError:
                    print("\t\t\t\u274C Ingresa un valor numerico")
        lista.append([nombre]+calificaciones)
        print("\t\t\t\u2705 Accion realizada con exito")
        print(lista)
        cursor=conexionBD.cursor()
        sql="insert into calificaciones (nombre, cal1, cal2, cal3) values ( %s, %s, %s, %s)"
        for i in range(0,len(lista)):
            val=(nombre,lista[i][1],lista[i][2],lista[i][3])
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")


def mostrar_calificaciones(listas):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      cursor=conexionBD.cursor()
      sql="select * from calificaciones"
      cursor.execute(sql)
      registros=cursor.fetchall()
      print("\t\t\t\U0001F440 Mostrar calificaciones \U0001F440")
      if registros:
        print(f"\t\t  {'Id':<10}{'Nombre':<15}{'Calificación 1':<20}{'Calificación 2':<20}{'Calificación 3':<20}")
        print("\t\t","-"*60)
        for fila in registros:
            print(f"\t\t  {fila[0]:<10}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("\t\t","-"*55)  
      else:
        print("\n\t .:: No hay calificaciones en el Sistema ::. ")      

def calcular_calificaciones(lista):
        borrarPantalla()
        print("	\t\t\U0001F4CA Promedio de los Alumnos \U0001F4CA")
        conexionBD=conectar()
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            sql="select * from calificaciones"
            cursor.execute(sql)
            registros=cursor.fetchall()
            print(f"\t\t{'Nombre':<15}  {'Promedio':<15} ")
            print("\t\t","-"*30)
            promedio_grupal=0
            for fila in registros:
                nombre=fila[1]
                promedio=(sum(fila [2:]))/3
                print(f"\t\t{nombre:<15}  {promedio:.2f} ")
                promedio_grupal+=promedio
            print("\t\t","-"*30)
            promedio_grupal=promedio_grupal/len(registros)
            print(f"\t\t\U0001F4C2 El promedio del grupo es: {promedio_grupal:.2f}")
        