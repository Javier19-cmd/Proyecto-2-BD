#Importando archivos.
from registro import *

#Página de inicio del programa.
def inicio():
    while True: #While para que la ejecución nunca termine.
        print("Bienvenido al sistema de streaming UVG\n")

        print("1. Iniciar sesión\n")

        print("2. Registrarse\n")

        print("3. Salir\n")

        try:
            opcion = int(input("Escoja la opción que desee \n"))

            if opcion == 1:
                print("Opción 1 elegida \n")
            elif opcion == 2: 
                print("Opción de registro elegida \n")
                registro() #Trayendo el método registro hasta este archivo.
            
            elif opcion==3:
                #Se cierra el programa.
                print("Se cerró el programa")

                break;
            else: 
                #Se eligió un número más allá del 3 ó más abajo que el 1. 
                print("Opción no válida \n")
        except:
            print("Se eligió una opción no numérica")

inicio() #Página de inicio.