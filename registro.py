import psycopg2 #Librería para la base de datos.
from datos import * #Jalando el archivo que tiene los datos de la BD.
import cryptocode

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

    print("La contraseña debe ser menor a 5 caracteres.")
    contraseña = input("Ingrese su contraseña: ")
    
    if len(contraseña) > 5:
        #Regresando al usuario a poner bien todos sus datos si en caso la contraseña excede los cinco caracteres
        print("Longitud no válida, favor ingrese todo bien otra vez")
        registro()

    passkey = 'UVG' #Llave para encriptar.

    conn = cryptocode.encrypt(contraseña, passkey) #Contraseña encriptada.

    correo = input("Ingrese su correo: ")

    print("\n")

    #Plan básico, estándar y avanzado.
    print("Los planes que existen son: ")
    print("1) Básico: Este plan es gratis")
    print("2) Estándar: Este plan es pagado y vale $3")
    print("3) Avanzado: Este plan es pagado y vale $5\n")
    plan = input("Ingrese su plan: ")

    insertar(nombre, apellido, usuario, conn, correo, plan) #Mandando los datos a la base de datos.

#Método para que se inserten los datos en la BD.
def insertar(nombre, apellido, usuario, conn, correo, plan):
    print("Se insertaron los datos: ")
    print(nombre)
    print(apellido)
    print(usuario)
    print(conn)
    print(correo)
    print(plan)

    #Comprobando que la contraseña sea la misma.
    llave = 'UVG' #Llave para desencriptar.
    des = cryptocode.decrypt(conn, llave) #Desencriptando mensaje.
    print(des)

registro()