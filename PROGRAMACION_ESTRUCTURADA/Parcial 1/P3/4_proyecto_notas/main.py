import funciones
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
          # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print("\n \tSe registro el ususario {nombre} {apellidos} correctamente")
            else:
                print("\n \t⚠️ No se pudo registrar el usuario, intente de nuevo más tarde ⚠️") 
              
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email, password)
            if len(lista_usuarios)>0:
             menu_notas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
                print("\n \t⚠️ No se pudo iniciar sesión, verifica tus credenciales ⚠️")
                funciones.esperarTecla()
            
               
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            Respuesta=nota.crear(usuario_id, titulo, descripcion)
            if Respuesta:
                print(f"\n \t Se creo la nota{titulo} correctamente")
            else:
                print("No fue posible crear esta nota intentalo mas tarde")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
              print("\n\tMostrar notas")
              print(f"{'ID':<10} {'titulo':<15}{'descripcion':<20} {'fecha':<10}")
              for fila in lista_notas:
                 print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<25}{fila[3]:<20}{fila[4]:}")
                 print(f"-"*80)
            else:
                print("No hay registros")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
              print("n\ t mostrar notas")
              print(f"{'ID':<10} {'titulo':<10} {'descripcion':<10} {'fecha':<10}")
              for fila in lista_notas:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
                print(f"-"*80)
            else:
                print("No hay registros")
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            Respuesta=nota.cambiar(id, titulo, descripcion)
            if Respuesta:
                print("Se actualizó la nota correctamente")
            else:
                print("No fue posible actualizar esta nota, intentalo mas tarde")
            funciones.esperarTecla()    
        elif opcion == '4' or opcion=="ELIMINAR": 
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
               print("\n\tMostrar notas")
               print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<25}{'Fecha':<20}")
               for fila in lista_notas:
                  for fila in lista_notas:
                   print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<25}{fila[3]:<20}{fila[4]:}")
               print("-"*80)
            else:
                 print("No hay registros")
                 funciones.esperarTecla()
                 return
            funciones.esperarTecla()
            respuesta = input("\n\t¿Estas seguro de eliminar una nota? (S/N): ").upper().strip()
            print(f"\n\t.:: {nombre} {apellidos}, vamos a borrar una Nota ::.\n")
            if respuesta == 'S':
               id = input("\t\tID de la nota a eliminar: ")
       
               resultado = nota.eliminar(id)
               if resultado:
                 print(f"Se borró la nota correctamente")
               else:
                print("No fue posible borrar esta nota, intentalo más tarde")
               funciones.esperarTecla()
        elif opcion == '5' or opcion=="Buscar":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a buscar una Nota ::. \n")
            id = input("\t\tID de la nota a buscar: ")
            lista_notas=nota.buscar(id)
            if len(lista_notas) > 0:
              print("\n\tMostrar notas")
              print(f"{'ID':<10} {'id_usuario':<15} {'titulo':<15}{'descripcion':<20} {'fecha':<10}")
              for fila in lista_notas:
                 print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<25}{fila[3]:<20}{fila[4]:}")
                 print(f"-"*80)
            else:
                print("No hay registros")
            funciones.esperarTecla()
        elif opcion == '6' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    

