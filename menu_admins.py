import psycopg2 #Librería para la base de datos.
from datos import * #Trayendo la información de la Base Datos.

#Este menú se va a enseñar una vez ya se haya iniciado sesión como administrador.
def menu_admin():
    while True: 
        print("1. Ver contenido")
        print("2. Ver usuarios")
        print("3. Ver contenido de anuncios")
        print("4. Salir \n")
        
        #Try-catch del menú.
        try: 
            decision = int(input("¿Cuál opción elige? "))
            if decision == 1:
                #Ver contenido.
                print("Hola")
            elif decision == 2:
                #Ver usuarios.
                print("Hola")
            elif decision == 3:
                #Ver contenido de anuncios. 
                print("Hola")
            elif decision == 4: 
                #Salir al menú principal.
                print("Saliendo....")
                break;
            else: #Opción no válida.
                print("Opción no válida.") 
        except: 
            #Opción no numérica elegida.
            print("Opción no numérica ingresada")