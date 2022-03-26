#Importando los datos de la BD.
from datos import * 
#Librería para la base de datos.
import psycopg2 
#Librería para encriptar las contraseñas.
import cryptocode
#Llamando al menú de administradores.
from menu_admins import *
#Llamando al menú comercial.
from menu_comercial import *

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

                normal() #Método para iniciar sesión con cuenta normal.

            elif eleccion == 2: 
                #Opción para iniciar sesión como administrador.
                print("Iniciar sesión como administrador")
                administrador() #Método para iniciar sesión con cuenta de administrador.
            elif eleccion == 3: 
                #Opción para no salir.
                print("Salir")
                break;
            else: 
                print("Opción no válida.")
        
        except: 
            print("Has ingresado una letra en vez de números")

#Método para iniciar sesión con cuenta normal.
def normal():
    
    usuario = input("Ingresa tu usuario: ") #Pidiendo usuario.
    contraseña = input("Ingresa tu contraseña: ")#Pidiendo contraseña.
    
    #Encriptando contraseña.
    passkey = 'UVG' #Llave para encriptar.

    conn = cryptocode.encrypt(contraseña, passkey) #Contraseña encriptada.

    #Imprimiendo datos.
    #print(usuario)
    #print(conn)

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #SQL para seleccionar usuario.
    sql = "SELECT usuario FROM datos_usuario WHERE usuario = %s"

    #Verificando que el usuario sí exista en la tabla.
    cursor1.execute(sql, (usuario,))
    rows=cursor1.fetchall()
    for row in rows:
        if usuario == row[0]: 
            print("Usuario encontrado")
        else: 
            print("Error")
    
    #Verificando que la contraseña exista en la base de datos.
    #Buscando contraseña.
    sql2 = "SELECT contraseña FROM datos_usuario WHERE usuario = %s"

    cursor1.execute(sql2,(usuario,)) #Jalando contraseñas.
    rows2=cursor1.fetchall()
    #print(contra)
    for row1 in rows2:
        a = row1[0] #Guardando la contraseña en una variable.
        decode = cryptocode.decrypt(a, "UVG") #Desencriptando la varialbe.
        print(decode) #Imprimiendo la variable.
        if contraseña == decode: 
            print("Contraseña correcta")
            menu_comercial() #Trayendo menú de opciones.
        else: #La contraseña no es igual.
            print("Contraseña incorrecta")
            #Enviando el usuario de la persona a una tabla de fracaso.
            sql3 = "INSERT INTO fracaso VALUES (%s)"
            #Enviando datos a la tabla de fracaso.
            cursor1.execute(sql3, (usuario,))
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

#Método para validar los datos de los administradores.
def administrador():
    print("Por favor ingrese sus datos de administrador \n")

    usuario = input("Ingresa tu usuario: ") #Pidiendo usuario.
    contraseña = input("Ingresa tu contraseña: ")#Pidiendo contraseña.
    
    #Encriptando contraseña.
    passkey = 'UVG' #Llave para encriptar.

    conn = cryptocode.encrypt(contraseña, passkey) #Contraseña encriptada.

    #Imprimiendo datos.
    #print(usuario)
    #print(conn)

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #SQL para seleccionar usuario.
    sql = "SELECT usuario FROM admins WHERE usuario = %s"

    #Verificando que el usuario sí exista en la tabla.
    cursor1.execute(sql, (usuario,))
    rows=cursor1.fetchall()
    for row in rows:
        if usuario == row[0]: 
            print("Usuario encontrado")
        else: 
            print("Error")
    
    #Verificando que la contraseña exista en la base de datos.
    #Buscando contraseña.
    sql2 = "SELECT contrasña FROM admins WHERE usuario = %s"

    cursor1.execute(sql2,(usuario,)) #Jalando contraseñas.
    rows2=cursor1.fetchall()
    #print(contra)
    for row1 in rows2:
        a = row1[0] #Guardando la contraseña en una variable.
        decode = cryptocode.decrypt(a, "UVG") #Desencriptando la varialbe.
        print(decode) #Imprimiendo la variable.
        if contraseña == decode: 
            print("Contraseña correcta")
            menu_admin() #Trayendo menú de opciones.
        else: #La contraseña no es igual.
            print("Contraseña incorrecta")
            #Enviando el usuario de la persona a una tabla de fracaso.
            sql3 = "INSERT INTO fracaso VALUES (%s)"
            #Enviando datos a la tabla de fracaso.
            cursor1.execute(sql3, (usuario,))
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

def desencriptar_contrasena(usuario):
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.