#Importando archivos.
from registro import *

#Registro de administradores.
from registro_admins import *

#Login de los usuarios.
from login import *

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
                
                #Opción para iniciar sesión.
                print("Opción 1 elegida \n")
                pagina() #Página para el inicio de sesión.

            elif opcion == 2: 

                #Opción para registrar usuarios.
                print("Opción de registro elegida \n")
                registro() #Trayendo el método registro hasta este archivo.
            
            elif opcion==3:
                #Opción para registrar administrador.
                print("Opción de registro de administrador elegida \n")

                registrar_admin() #Llamando al método que registra al administrador en la BD.

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