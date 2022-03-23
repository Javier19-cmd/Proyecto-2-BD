#Importando archivos.
from registro import *

#Página de inicio del programa.
def inicio():
    while True: #While para que la ejecución nunca termine.
        print("Bienvenido al sistema de streaming UVG\n")

        print("1. Iniciar sesión\n")

        print("2. Registrarse\n")

        print("3. Registrar administrador \n")

        print("4. Salir\n")

        #Try-except para evitar que se ingrese una opción no numérica.
        try:
            opcion = int(input("Escoja la opción que desee \n")) #Opción a elegir.
            print("\n") #Salto de línea para que se vea mejor.
 
            if opcion == 1:
                print("Opción 1 elegida \n")
            elif opcion == 2: 
                print("Opción de registro elegida \n")
                registro() #Trayendo el método registro hasta este archivo.
            
            elif opcion==3:
                #Opción para registrar administrador.
                print("Opción de registro de administrador elegida \n")

            elif opcion == 4: 
                #Cerrar programa.
                print("Se cerró el programa. \n")
                break;

            else: 
                #Se eligió un número más allá del 3 ó más abajo que el 1. 
                print("Opción no válida \n")
        except:
            print("Se eligió una opción no numérica \n")

inicio() #Página de inicio.