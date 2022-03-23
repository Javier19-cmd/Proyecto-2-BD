#Importando los datos de la BD.
from datos import *
#Librería para la base de datos.
import psycopg2 
#Librería para encriptar las contraseñas.
import cryptocode

def registrar_admin(): #Método que sirve para registrar a los administradores.
    
    print("Página para registrar administadores \n")

    #Datos del registrador.
    nombre = input("Ingrese el nombre del administrador: ")

    apellido = input("Ingrese el apellido del administrador: ")

    usuario = input("Ingrese el usuario del administrador: ")

    print("La contraseña debe ser de cinco caracteres.")

    contraseña = input("Ingrese la contraseña: ")

    if len(contraseña) > 5:
        #Regresando al usuario a poner bien todos sus datos si en caso la contraseña excede los cinco caracteres.
        print("Longitud no válida, favor ingrese todo bien otra vez")
        registrar_admin()
    elif len(contraseña) < 5:
        #Regresando al usuario a poner todos su datos si en caso la contraseña es menor a cinco caracteres.
        print("Longitud no válida, favor ingrese todo bien otra vez")
        registrar_admin()
    
    #Encriptando contraseña
    passkey = 'UVG' #Llave para encriptar.

    conn = cryptocode.encrypt(contraseña, passkey) #Contraseña encriptada.

    insertar(nombre, apellido, usuario, conn) #Enviando a insertar los datos.

#Método para insertar contraseñas.
def insertar(nombre, apellido, usuario, contraseña):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #Seleccionando los usuarios de la tabla.
    #Verificando que el usuario ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez todo.
    cursor1.execute("SELECT usuario FROM admins")
    rows=cursor1.fetchall()
    for row in rows:
        print(row[0])
        if usuario == row[0]:
            print("Usuario existente, favor regresar a ingresar bien los datos")
            registrar_admin() #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
    
    #Imprimiendo los datos que se insertarán en la tabla de usuarios.
    print("Se insertaron los datos: ")
    print(nombre)
    print(apellido)
    print(usuario)
    print(contraseña)

    #SQL para insertar los datos en una tabla.
    sql = "INSERT INTO admins VALUES (%s, %s, %s, %s)"
    
    cursor1.execute(sql, (nombre, apellido, usuario, contraseña)) #Insertando formalmente los datos.

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()