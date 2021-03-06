"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
#Importando los datos de la BD.
from datos import * 
from conexion import *
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
        #try: 
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
        
        #except: 
         #   print("Has ingresado una letra en vez de números")

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
    conexion1 = connect()

    setConnection(conexion1) #Conexión a la base de datos.

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
        #print(decode) #Imprimiendo la variable.
        if contraseña == decode: 
            print("Contraseña correcta")
            setConnection(conexion1)
            sql6 = "SET myapp.username = %s"
            cursor1.execute(sql6, (usuario,))
            conexion1.commit()
            traer_perfiles(usuario) #Trayendo menú de opciones.
            
        else: #La contraseña no es igual.
            print("Contraseña incorrecta")
            #Enviando el usuario de la persona a una tabla de fracaso.
            sql3 = "INSERT INTO fracaso VALUES (%s)"
            #Enviando datos a la tabla de fracaso.
            cursor1.execute(sql3, (usuario,))
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            disconnect(conexion1)

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
    conexion1 = connect()

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #SQL para seleccionar usuario.
    sql = "SELECT usuario FROM admins WHERE usuario = %s"

    #Verificando que el usuario sí exista en la tabla.
    cursor1.execute(sql, (usuario,))
    rows=cursor1.fetchall()
    
    a = []

    #Guardando el usuario que se trajo.
    for cosa in rows:
        a.append(cosa[0])

    print(a)

    if usuario in a: #Si el usuario existe.
        print("Usuario encontrado")

    #Viendo si el usuario ya entró o no.
    sqls = "SELECT ingreso FROM admins WHERE usuario = %s"

    cursor1.execute(sqls, (usuario,))
    rowss=cursor1.fetchall()

    #Lista para el parámetro ingreso.
    entrada = []

    #Guardando el ingreso que se trajo.
    for cosas in rowss:
        entrada.append(cosas[0])
    
    confir = 0

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
            if confir in entrada:
                setConnection(conexion1)
                # execute SET myapp.username = 'usuario' query;
                sql6 = "SET myapp.username = %s"
                cursor1.execute(sql6, (usuario,))
                conexion1.commit()
                sqlsa = "UPDATE admins SET ingreso = %s WHERE usuario = %s"
                confr = 1
                cursor1.execute(sqlsa, (confr, usuario,))
                conexion1.commit()
                menu_admin(usuario) #Trayendo menú de opciones.
            else: 
                print("Usuario activo")
                break
        else: #La contraseña no es igual.
            print("Contraseña incorrecta")
            #Enviando el usuario de la persona a una tabla de fracaso.
            sql3 = "INSERT INTO fracaso VALUES (%s)"
            
            pagina()  

            #Enviando datos a la tabla de fracaso.
            cursor1.execute(sql3, (usuario,))
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            disconnect(conexion1)
