import psycopg2 #Librería para la base de datos.
from datos import * #Jalando el archivo que tiene los datos de la BD.

def abrir_BD(): #Método que servirá para poder ingresar los datos del usuario en la base de datos.
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

#Archivo que se encarga de registrar a las personas en la base de datos.
def registro():
    #Menú para registrar a las personas en la base de datos.
    print("Bienvenid@ a la página de registro de la plataforma de streaming \n")

    #Datos que se le pedirán a los usuarios: 
    nombre = input("Ingrese su nombre: ")

    apellido = input("Ingrese su apellido: ")

    usuario = input("Ingrese su usuario: ")

    contraseña = input("Ingrese su contraseña: ")

    correo = input("Ingrese su correo: ")

    print("\n")

    #Plan básico, estándar y avanzado.
    print("Los planes que existen son: ")
    print("1) Básico: Este plan es gratis")
    print("2) Estándar: Este plan es pagado y vale $3")
    print("3) Avanzado: Este plan es pagado y vale $5\n")
    plan = input("Ingrese su plan: ")