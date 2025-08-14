
def borrarPantalla():
    import os 
    os.system('cls')

def esperarTecla():
    input("\nPresiona Enter para continuar...")

def menu_principal():
    print("\n=== SISTEMA DE GESTIÓN DE VUELOS ===")
    print("1. Pasajero")
    print("2. Administrador")
    print("3. Salir")
    return input("\nSeleccione una opción: ").strip()

def menu_pasajero():
    print("\n=== MENÚ PASAJERO ===")
    print("1. Ver Vuelos Disponibles")
    print("2. Reservar Vuelo")
    print("3. Buscar Vuelo")
    print("4. Cancelar Reserva")
    print("5. Volver al Menú Principal")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion   

def menu_administradores(nombre):
    print(f"\n=== MENÚ ADMINISTRADOR: {nombre} ===")
    print("1. Ver Vuelos Disponibles")
    print("2. Buscar Vuelo")
    print("3. Eliminar Reserva")
    print("4. Eliminar Vuelo")
    print("5. agregar Vuelo")
    print("6. Modificar Vuelo" )
    print("7. Ver Reservas")
    print("8. Ver Administradores")
    print("9. modificar Reserva")
    print("10. Eliminar pasajero")
    print("11. Volver al Menú Principal")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion