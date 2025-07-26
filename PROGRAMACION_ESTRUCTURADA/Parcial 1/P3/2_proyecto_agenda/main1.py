import agenda2

def main():
    agenda_contactos={}
    opcion=True

    while opcion:
        agenda2.borrarPantalla()
        opcion=agenda2.menu_principal()

        if opcion=="1":
            agenda2.agregar_contacto(agenda_contactos)
            agenda2.esperarTecla()
            
        elif opcion=="2":
          agenda2.mostrar_contactos(agenda_contactos)
          agenda2.esperarTecla()   
          
        elif opcion=="3":
          agenda2.buscar_contacto(agenda_contactos)
          agenda2.esperarTecla()
        elif opcion=="4":
          agenda2.borrar_contacto(agenda_contactos)
          agenda2.esperarTecla()
        elif opcion=="5":
           agenda2.modificar_contacto(agenda_contactos)
           agenda2.esperarTecla()
        elif opcion=="6":
          agenda2.borrarPantalla()
          print(" Programa finalizado.")
          opcion=False   
        else:
           opcion=True
           print(" Opcion no válida. Intenta de nuevo.")

if __name__=="__main__":
   main()                 
