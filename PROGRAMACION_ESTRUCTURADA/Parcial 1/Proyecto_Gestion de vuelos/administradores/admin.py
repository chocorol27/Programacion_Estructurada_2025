from ConexionBd import *
import datetime


def registrar(nombre, usuario, contrasena):
    try:
        cursor.execute("INSERT INTO administradores (nombre,usuario,password) VALUES (%s, %s, %s)", (nombre, usuario, contrasena,))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al registrar administrador:", e)
        return False
    
def login(usuario, contrasena):
    try:
        cursor.execute("SELECT * FROM administradores WHERE usuario=%s AND password=%s", (usuario, contrasena))
        return cursor.fetchone()
    except Exception as e:
        print("Error en login:", e)
        return None
    
def mostrar():
    try:
        cursor.execute("SELECT * FROM vuelos")
        return cursor.fetchall()
    except:
        return []
    


def buscar_vuelo(origen, destino):
    try:
        cursor.execute("SELECT * FROM vuelos WHERE origen=%s AND destino=%s", (origen, destino))
        return cursor.fetchall()
    except:
        return []
    
def eliminar(id_vuelo, num_asiento):
    try:
        cursor.execute("DELETE FROM reservas WHERE id_vuelo = %s AND num_asiento = %s", (id_vuelo, num_asiento))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar_reservas():
    try:
        cursor.execute("SELECT * FROM reservas ")
        return cursor.fetchall()
    except:
        return []


def eliminar_vuelo(id):
    try:
        cursor.execute("DELETE FROM vuelos WHERE id= %s", (id,))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al eliminar vuelo:", e)
        return False

def modificar_vuelo(id,numero=None, origen=None,destino=None, hora_salida=None, hora_llegada=None, fecha_salida=None):
    try:
        campos = []
        valores = []
        
        if numero:
            campos.append("numero = %s")
            valores.append(numero)
        if origen:
            campos.append("origen = %s")
            valores.append(origen)
        if destino:
            campos.append("destino = %s")
            valores.append(destino)
        if hora_salida:
            campos.append("hora_salida = %s")
            valores.append(hora_salida)
        if hora_llegada:
            campos.append("hora_llegada = %s")
            valores.append(hora_llegada)
        if fecha_salida:
            campos.append("fecha_salida = %s")
            valores.append(fecha_salida)
        if not campos:
            return False  # No hay cambios

        valores.append(id)
        sql = f"UPDATE vuelos SET {', '.join(campos)} WHERE id = %s"
        cursor.execute(sql, tuple(valores))
        conexion.commit()
        return True

    except Exception as e:
        print("Error al modificar vuelo:", e)
        return False
def agregar_vuelo(numero, origen, destino, hora_salida, hora_llegada, fecha_salida):
    try:
        cursor.execute("INSERT INTO vuelos (numero, origen, destino, hora_salida, hora_llegada, fecha_salida) VALUES (%s, %s, %s, %s, %s, %s)", (numero, origen, destino, hora_salida, hora_llegada, fecha_salida))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al agregar vuelo:", e)
        return False
    
def mostrar_administradores():
    try:
        cursor.execute("SELECT * FROM administradores")
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar administradores:", e)
        return []
    
def modificar_reserva(id, id_pasajero=None, id_vuelo=None, num_asiento=None, fecha_reserva=None):
    try:
        campos = []
        valores = []
        if id_pasajero:
            campos.append("id_pasajero = %s")
            valores.append(id_pasajero)
        if id_vuelo:
            campos.append("id_vuelo = %s")
            valores.append(id_vuelo)
        if num_asiento:
            campos.append("num_asiento = %s")
            valores.append(num_asiento)
        if fecha_reserva:
            campos.append("fecha_reserva = %s")
            valores.append(fecha_reserva)
        if not campos:
            return False  # No hay cambios

        valores.append(id)
        sql = f"UPDATE reservas SET {', '.join(campos)} WHERE id = %s"
        cursor.execute(sql, tuple(valores))
        conexion.commit()
        return True

    except Exception as e:
        print("Error al modificar reserva:", e)
        return False
def eliminar_pasajero(id):
    try:
        cursor.execute("DELETE FROM pasajeros WHERE id = %s", (id,))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al eliminar pasajero:", e)
        return False
def mostrar_pasajeros():
    try:
        cursor.execute("SELECT * FROM pasajeros")
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar pasajeros:", e)
        return []