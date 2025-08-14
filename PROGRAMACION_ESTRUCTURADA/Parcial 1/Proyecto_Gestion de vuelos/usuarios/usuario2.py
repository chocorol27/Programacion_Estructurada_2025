from ConexionBd import *
import datetime


def registrar(nombre,usuario,contrasena,email,telefono):
    try:
        cursor.execute("INSERT INTO pasajeros (nombre, usuario, password, email, telefono) VALUES (%s, %s, %s, %s, %s)", (nombre, usuario, contrasena, email, telefono))
        conexion.commit()  # Asegúrate de hacer commit para guardar los cambios
        return True
    except:
        return False
    
def login(email, contrasena):
    try:
        cursor.execute("SELECT * FROM pasajeros WHERE email=%s AND password=%s", (email, contrasena))
        return cursor.fetchone()
    except Exception as e:
        print("Error en login:", e)
        return None
    
def mostrar():
    try:
        cursor.execute("select * from vuelos",)
        return cursor.fetchall()  # Retorna todas las notas del usuario
    except:
        return []
    

def reservar_vuelo(nombre, id_vuelo, num_asiento, fecha_reserva=datetime.datetime.now()):
    try:
        # Busca el id del pasajero por su nombre
        cursor.execute("SELECT id FROM pasajeros WHERE nombre=%s", (nombre,))
        pasajero = cursor.fetchone()
        
        if not pasajero:
            return False
        
        id_pasajero = pasajero[0]
    
        cursor.execute("INSERT INTO reservas (id_pasajero, id_vuelo, num_asiento, fecha_reserva) VALUES (%s, %s, %s, %s)", (id_pasajero, id_vuelo, num_asiento, fecha_reserva))
        
        conexion.commit()
        return True

    except Exception as e:
        print("Error al reservar vuelo:", e)
        return False

def buscar_vuelo(origen, destino):
    try:
        cursor.execute("SELECT * FROM vuelos WHERE origen=%s AND destino=%s ", (origen, destino,))
        return cursor.fetchall()
    except :
        return []
    
def eliminar(id_vuelo, num_asiento):
    try:
        cursor.execute("delete from reservas WHERE id_vuelo = %s and num_asiento =%s" , (id_vuelo,num_asiento))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar_reservas(id_pasajero):
    try:
        cursor.execute("SELECT * FROM reservas WHERE id_pasajero = %s", (id_pasajero,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar reservas:", e)
        return []