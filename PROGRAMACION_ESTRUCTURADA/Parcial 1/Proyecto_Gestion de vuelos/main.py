import funciones
from usuarios import usuario2
from administradores import admin
import getpass

def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menu_principal()  # ahora con 1. Pasajero 2. Administrador 3. Salir

        if opcion == "1" or opcion.upper() == "PASAJERO":
            funciones.borrarPantalla()
            print("\n\t..:: MENÚ PASAJERO ::..")
            print("\t1. Registrarse")
            print("\t2. Iniciar sesión")
            print("\t3. Volver al menú principal")
            subop = input("\n\tSelecciona una opción: ").strip()

            if subop == "1":
                funciones.borrarPantalla()
                print("\n \t..:: Registro de Pasajero ::..")
                nombre = input("\tNombre completo: ").upper().strip()
                usuario_p = input("\tNombre de usuario: ").strip()
                password = getpass.getpass("\tContraseña: ").strip()
                email = input("\tEmail: ").lower().strip()
                telefono = input("\tTeléfono: ").strip()
                

                registrado = usuario2.registrar(nombre, usuario_p, password, email, telefono)
                if registrado:
                    print(f"\n✅ Usuario {usuario_p} registrado correctamente.")
                else:
                    print("\n⚠️ No se pudo registrar el usuario.")
                funciones.esperarTecla()

            elif subop == "2":
                funciones.borrarPantalla()
                print("\n\t..:: Iniciar Sesión como Pasajero ::..")
                email = input("\tIngresa tu E-mail: ").lower().strip()
                password = getpass.getpass("\tIngresa tu contraseña: ").strip()
                resultado = usuario2.login(email, password)  # Debes tener esta función en usuario.py
                if resultado:
                    print(f"\n✅ Bienvenido, {resultado[1]}!")
                    menu_pasajero(resultado[1], resultado[0])  # Pasa nombre y id

                else:
                    print("\n⚠️ No se pudo iniciar sesión, verifica tus credenciales ⚠️")
                    funciones.esperarTecla()


                

        elif opcion == "2" or opcion.upper() == "ADMINISTRADOR":
             funciones.borrarPantalla()
             print("\n\t..:: MENÚ Admin ::..")
             print("\t1. Registrarse")
             print("\t2. Iniciar sesión")
             print("\t3. Volver al menú principal")
             subop = input("\n\tSelecciona una opción: ").strip()

            
             if subop == "1":
                    funciones.borrarPantalla()
                    print("\n \t..:: Registro de Administrador ::..")
                    nombre = input("\tNombre completo: ").upper().strip()
                    usuario= input("\tNombre de usuario: ").strip()
                    password = getpass.getpass("\tContraseña: ").strip()
                   
                    registrado = admin.registrar(nombre, usuario, password, )
                    if registrado:
                        print(f"\n✅ Usuario {usuario} registrado correctamente.")
                    else:
                        print("\n⚠️ No se pudo registrar el usuario.")
                    funciones.esperarTecla()
             elif subop == "2":
                    funciones.borrarPantalla()
                    print("\n\t..:: Iniciar Sesión como Administrador ::..")
                    usuario_a = input("\tIngresa tu usuario: ").lower().strip()
                    password = getpass.getpass("\tIngresa tu contraseña: ").strip()
                    resultado = admin.login(usuario_a, password)  # Debes tener esta función en usuario.py
                    if resultado:
                       print(f"\n✅ Bienvenido, {resultado[1]}!")
                       menu_administradores(resultado[1], resultado[0])
                    else:
                     print("\n⚠️ No se pudo iniciar sesión, verifica tus credenciales ⚠️")
                     funciones.esperarTecla()


                    







            


def menu_pasajero(nombre, id_pasajero):
    while True:
        funciones.borrarPantalla()
        opcion = funciones.menu_pasajero()
        print(f"Bienvenido {nombre}has iniciado sesion")
        
        if opcion == "1":
            print(f"\n\t..:: Ver Vuelos Disponibles ::..")
            funciones.borrarPantalla()
            #Agregar codigo  
            vuelos = usuario2.mostrar()
            if len(vuelos) > 0:
              print("\n\tMostrar Vuelos Disponibles")
              print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
              for fila in vuelos:
                print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
                print(f"-"*90)
            funciones.esperarTecla()

        elif opcion == "2":
            print(f"\n\t..:: Reservar Vuelo ::..")
            vuelos=usuario2.mostrar()
            if len(vuelos) > 0:
                print("\n\tSelecciona un vuelo para reservar:")
                print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
                for fila in vuelos:
                     print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
                     print(f"-"*90)
                id_vuelo= input("\n\tIngrese el ID del vuelo que desea reservar: ").strip()
                num_asiento=input("\tIngrese el número de asiento: ").strip()
                exito = usuario2.reservar_vuelo(nombre, id_vuelo, num_asiento)
                if exito:
                    print(f"\n✅ Vuelo {id_vuelo} reservado exitosamente.")
                else:
                    print("\n❌ No se pudo reservar el vuelo. Verifique el ID e intente nuevamente.")   
            else:
                print("\n⚠️ No hay vuelos disponibles.")
            
            
            
            funciones.esperarTecla()

        elif opcion == "3":
            print(f"\n\t..:: Buscar Vuelo ::..")
            origen = input("\tIngrese el origen: ").strip().upper()
            destino = input("\tIngrese el destino: ").strip().upper()
            resultados = usuario2.buscar_vuelo(origen, destino)
            if resultados:
                encontrados=+1
                print(f"\n✅ Se encontraron {encontrados} vuelos:")
                print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
                for fila in resultados:
                    print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
                    print(f"-"*90)
          

            funciones.esperarTecla()

        elif opcion == "4":
            print(f"\n\t..:: Ver Reservas ::..")
            reservas = usuario2.mostrar_reservas(id_pasajero)
            if reservas:
                print(f"\n\tTus Reservas:")
                print(f"{'id':<10}{'id_pasajero':<15}{'id_vuelo':<15}{'num_asiento':<15}{'Fecha_reserva':<15}")
                for reserva in reservas:
                    print(f"{reserva[0]:<10}{reserva[1]:<15}{reserva[2]:<15}{reserva[3]:<15}{str(reserva[4]):<15}")
                    print(f"-"*90)
            print("Quieres eliminar una reserva S/N?")
            eliminar = input("\tIngrese S para eliminar o N para salir: ").strip().upper()
            if eliminar == "S":
                id_vuelo = input("\tIngrese el ID del vuelo a eliminar: ").strip()
                num_asiento = input("\tIngrese el número de asiento: ").strip()
                exito = usuario2.eliminar(id_vuelo, num_asiento)
                if exito:
                    print(f"\n✅ Reserva eliminada exitosamente.")
                else:
                    print("\n❌ No se pudo eliminar la reserva. Verifique el ID e intente nuevamente.")
            funciones.esperarTecla()
           
        elif opcion == "5":
            break

        else:
            print("\n❌ Opción no válida.")
            funciones.esperarTecla()



def menu_administradores(nombre,id):
    while True:
        funciones.borrarPantalla()
        opcion = funciones.menu_administradores(nombre)
        
        if opcion == "1":
            print(f"\n\t..:: Ver Vuelos Disponibles ::..")
            vuelos = admin.mostrar()
            if len(vuelos) > 0:
                print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
                for fila in vuelos:
                    print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
            else:
                print("\n⚠️ No hay vuelos disponibles.")
            funciones.esperarTecla()

        elif opcion == "2":
            print(f"\n\t..:: Buscar Vuelo ::..")
            origen = input("\tIngrese el origen: ").strip().upper()
            destino = input("\tIngrese el destino: ").strip().upper()
            resultados = admin.buscar_vuelo(origen, destino)
            if resultados:
                encontrados=+1
                print(f"\n✅ Se encontraron {encontrados} vuelos:")
                print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
                for fila in resultados:
                    print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
                    print(f"-"*90)
            else:
                print("\n⚠️ No se encontraron vuelos.")
            funciones.esperarTecla()

        elif opcion == "3":
            print(f"\n\t..:: Eliminar Reserva ::..")
            reservas = admin.mostrar_reservas()
            if reservas:
                print(f"\n\tReservas Actuales:")
                print(f"{'id':<10}{'id_pasajero':<15}{'id_vuelo':<15}{'num_asiento':<15}{'Fecha_reserva':<15}")
                for reserva in reservas:
                    print(f"{reserva[0]:<10}{reserva[1]:<15}{reserva[2]:<15}{reserva[3]:<15}{str(reserva[4]):<15}")
                    print(f"-"*90)
            else:
                print("\n⚠️ No hay reservas disponibles.")
            
            eliminar = input("¿Quieres eliminar una reserva?").strip().upper()
            if eliminar == "S":
                funciones.esperarTecla()
            id_vuelo = input("\tIngrese el ID del vuelo: ").strip()
            num_asiento = input("\tIngrese el número de asiento: ").strip()
            exito = admin.eliminar(id_vuelo, num_asiento)
            if exito:
                print(f"\n✅ Reserva del vuelo {id_vuelo} eliminada exitosamente.")
            else:
                print("\n❌ No se pudo eliminar la reserva. Verifique el ID e intente nuevamente.")
            funciones.esperarTecla()
        elif opcion == "4":
            print(f"\n\t..:: Eliminar Vuelo ::..")
            vuelos = admin.mostrar()
            if len(vuelos) > 0:
                print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
                for fila in vuelos:
                    print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
                print(f"-"*90)
            else:
                print("\n⚠️ No hay vuelos disponibles.")
            opcion = input("\t¿Desea eliminar un vuelo? (S/N): ").strip().upper()
            if opcion == "S":

              id_vuelo = input("\tIngrese el ID del vuelo a eliminar: ").strip()
              exito = admin.eliminar_vuelo(id)
            if exito:
                print(f"\n✅ Vuelo {id_vuelo} eliminado exitosamente.")
            else:
                print("\n❌ No se pudo eliminar el vuelo. Verifique el ID e intente nuevamente.")
            funciones.esperarTecla()
        elif opcion == "5":
            print(f"\n\t..:: Agregar Vuelo ::..")
            numero = input("\tNúmero de vuelo: ").strip().upper()
            origen = input("\tOrigen: ").strip().upper()
            destino = input("\tDestino: ").strip().upper()
            hora_salida = input("\tHora de salida (HH:MM): ").strip()
            hora_llegada = input("\tHora de llegada (HH:MM): ").strip()
            fecha_salida = input("\tFecha de salida (YYYY-MM-DD): ").strip()

            exito = admin.agregar_vuelo(numero, origen, destino, hora_salida, hora_llegada, fecha_salida)
            if exito:
                print(f"\n✅ Vuelo {numero} agregado exitosamente.")
            else:
                print("\n❌ No se pudo agregar el vuelo. Verifique los datos e intente nuevamente.")
            funciones.esperarTecla()
        elif opcion == "6":
           # ...en la opción 6 del menú de administrador...
         print(f"\n\t..:: Modificar Vuelo {id} ::..")
         print(f"{'ID':<5}{'Numero':<10}{'Origen':<15}{'Destino':<15}{'Hora Salida':<15}{'Hora Llegada':<15}{'Fecha Salida':<15}")
         vuelos = admin.mostrar()
         if len(vuelos) > 0:
                for fila in vuelos:
                    print(f"{fila[0]:<5}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{str(fila[4]):<15}{str(fila[5]):<15}{str(fila[6]):<15}")
                print(f"-"*90)
         id = input("\tIngrese el ID del vuelo a modificar: ").strip()
         numero = input("\tNuevo número de vuelo (dejar en blanco para no modificar): ").strip().upper() or None
         origen = input("\tNuevo origen (dejar en blanco para no modificar): ").strip().upper() or None
         destino = input("\tNuevo destino (dejar en blanco para no modificar): ").strip().upper() or None
         hora_salida = input("\tNueva hora de salida (HH:MM, dejar en blanco para no modificar): ").strip() or None
         hora_llegada = input("\tNueva hora de llegada (HH:MM, dejar en blanco para no modificar): ").strip() or None
         fecha_salida = input("\tNueva fecha de salida (YYYY-MM-DD, dejar en blanco para no modificar): ").strip() or None
         exito = admin.modificar_vuelo(id, numero, origen, destino, hora_salida, hora_llegada, fecha_salida)
         if exito:
             print(f"\n✅ Vuelo {id} modificado exitosamente.")
         else:
             print("\n❌ No se pudo modificar el vuelo. Verifique los datos e intente nuevamente.")
         funciones.esperarTecla()
            
        elif opcion == "7":
            print("\n\t..:: Ver reservas::..")
            reservas = admin.mostrar_reservas()
            if reservas:
                print(f"\n\tReservas Actuales:")
                print(f"{'id':<10}{'id_pasajero':<15}{'id_vuelo':<15}{'num_asiento':<15}{'Fecha_reserva':<15}")
                for reserva in reservas:
                    print(f"{reserva[0]:<10}{reserva[1]:<15}{reserva[2]:<15}{reserva[3]:<15}{str(reserva[4]):<15}")
                    print(f"-"*90)
            else:
                print("\n⚠️ No hay reservas disponibles.")
            funciones.esperarTecla()
        elif opcion == "8":
            print("\n\t..:: Ver administradores::..")
            adminst = admin.mostrar_administradores()
            if adminst:
                print(f"\n\tAdministradores Actuales:")
                print(f"{'ID':<5}{'Nombre':<20}{'Usuario':<15}")
                for adn in adminst:
                    print(f"{adn[0]:<5}{adn[1]:<20}{adn[2]:<15}")
                    print(f"-"*90)
        elif opcion == "9":
            print("\n\t..:: Modificar Reserva ::..")
            reservas = admin.mostrar_reservas()
            if reservas:
                print(f"\n\tReservas Actuales:")
                print(f"{'id':<10}{'id_pasajero':<15}{'id_vuelo':<15}{'num_asiento':<15}{'Fecha_reserva':<15}")
                for reserva in reservas:
                    print(f"{reserva[0]:<10}{reserva[1]:<15}{reserva[2]:<15}{reserva[3]:<15}{str(reserva[4]):<15}")
                    print(f"-"*90)
            else:
                print("\n⚠️ No hay reservas disponibles.")
            opciones = input("¿Quieres modificar una reserva? S/N: ").strip().upper()
            if opciones =="S":
                funciones.esperarTecla()
            id_reserva = input("\tIngrese el ID de la reserva a modificar: ").strip()
            id_vuelo = input("\tNuevo ID de vuelo (dejar en blanco para no modificar): ").strip() or None
            num_asiento = input("\tNuevo número de asiento (dejar en blanco para no modificar): ").strip() or None
            fecha_reserva = input("\tNueva fecha de reserva (YYYY-MM-DD, dejar en blanco para no modificar): ").strip() or None
            exito = admin.modificar_reserva(id, id_vuelo, num_asiento,fecha_reserva=None)
            if exito:
                print(f"\n✅ Reserva {id_reserva} modificada exitosamente.")
            else:
                print("\n❌ No se pudo modificar la reserva. Verifique los datos e intente nuevamente.")
        elif opcion == "10":
            print("\n\t..:: eliminar pasajero ::..")
            pasajeros = admin.mostrar_pasajeros()
            if pasajeros:
                print(f"\n\tPasajeros Actuales:")
                print(f"{'ID':<5}{'Nombre':<20}{'Usuario':<15}{'Email':<25}{'Teléfono':<15}")
                for pas in pasajeros:
                    print(f"{pas[0]:<5}{pas[1]:<20}{pas[2]:<15}{pas[3]:<25}{pas[4]:<15}")
                    print(f"-"*90)
            else:
                print("\n⚠️ No hay pasajeros disponibles.")
            opciones = input("¿Quieres eliminar un pasajero? S/N: ").strip().upper()
            if opciones =="S":
                funciones.esperarTecla()    
            id = input("\tIngrese el ID del pasajero a eliminar: ").strip()
            exito = admin.eliminar_pasajero(id)
            if exito:
                print(f"\n✅ Pasajero {id} eliminado exitosamente.")
            else:
                print("\n❌ No se pudo eliminar el pasajero. Verifique el ID e intente nuevamente.")
        elif opcion == "11":
            break
            



        

if __name__ == "__main__":
    main()