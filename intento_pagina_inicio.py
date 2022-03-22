#Importando archivos.
from registro import *

#Página de inicio del programa.
def inicio():
    while True: #While para que la ejecución nunca termine.
        print("Bienvenido al sistema de streaming UVG\n")

        print("1. Iniciar sesión\n")

        print("2. Registrarse\n")

        opcion = int(input("Escoja la opción que desee \n"))

        if opcion == 1:
            print("Opción 1 elegida \n")
        elif opcion == 2: 
            print("Opción de registro elegida \n")
            registro() #Trayendo el método registro hasta este archivo.
        else: 
            print("Opción no válida \n")
        

inicio() #Página de inicio.