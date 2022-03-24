#Importando los datos de la BD.
from datos import * 
#Librería para la base de datos.
import psycopg2 
#Librería para encriptar las contraseñas.
import cryptocode

#Método que sirve para poderle desplegar las opciones al usuario.
def pagina():
    while True:
        
        print("Bienvenido a la página de login \n")
        print("Elige la opción que te corresponda \n")
        print("1) Cuenta convencional")
        print("2) Cuenta de administrador")
        print("3) Salir \n")

        #Try-catch para evitar que el usuario no meta letras en vez de números.
        try: 
            eleccion = int(input("Ingresa la opción que desees: "))

            if eleccion == 1:
                #Opción para iniciar sesión con cuenta normal.
                print("Iniciar sesión con cuenta normal")
            elif eleccion == 2: 
                #Opción para iniciar sesión como administrador.
                print("Iniciar sesión como administrador")
            elif eleccion == 3: 
                #Opción para no salir.
                print("Salir")
                break;
            else: 
                print("Opción no válida.")
        
        except: 
            print("Has ingresado una letra en vez de números")