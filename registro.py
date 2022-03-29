"""
Referencias: 

1. Librería de cryptocode: https://www.delftstack.com/es/howto/python/python-encrypt-string/

"""
import psycopg2 #Librería para la base de datos.
from datos import * #Jalando el archivo que tiene los datos de la BD.
import cryptocode   #Librería para encriptar las contraseñas.
from perfiles import * #Llamando al archivo de perfiles, para poder registrarlos en otra tabla de la base de datos.

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

    print("La contraseña debe de 5 caracteres.")
    contraseña = input("Ingrese su contraseña: ")
    
    if len(contraseña) > 5:
        #Regresando al usuario a poner bien todos sus datos si en caso la contraseña excede los cinco caracteres.
        print("Longitud no válida, favor ingrese todo bien otra vez")
        registro()
    elif len(contraseña) < 5:
        #Regresando al usuario a poner todos su datos si en caso la contraseña es menor a cinco caracteres.
        print("Longitud no válida, favor ingrese todo bien otra vez")
        registro()

    #Encriptando contraseña.
    passkey = 'UVG' #Llave para encriptar.

    conn = cryptocode.encrypt(contraseña, passkey) #Contraseña encriptada.

    correo = input("Ingrese su correo: ")

    print("\n")

    #Plan básico, estándar y avanzado.
    print("Los planes que existen son: ")
    print("1) Básico: Este plan es gratis")
    print("2) Estándar: Este plan es pagado y vale $3")
    print("3) Avanzado: Este plan es pagado y vale $5\n")
    
    try:
        plan = int(input("Ingrese su plan: "))

        insertar(nombre, apellido, usuario, conn, correo, plan) #Mandando los datos a la base de datos.
    except:
        print("Opción no numérica")
#Método para que se inserten los datos en la BD.
def insertar(nombre, apellido, usuario, conn, correo, plan):
    
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
    cursor1.execute("SELECT usuario FROM datos_usuario")
    rows=cursor1.fetchall()
    for row in rows:
        #print(row[0])
        if usuario == row[0]:
            print("Usuario existente, favor regresar a ingresar bien los datos")
            registro() #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
    
    """
    #Seleccionando las contraseñas de la tabla.
    #Verificando que la contraseña ingresada no exista en la tabla.
    cursor1.execute("SELECT contraseña FROM datos_usuario")
    rows2=cursor1.fetchall()
    for row in rows2:
        a = row[0]
        decode = cryptocode.decrypt(a, "UVG") #Desencriptando la varialbe que trae a la contraseña desde la base de datos.
        decode2 = cryptocode.decrypt(conn, "UVG") #Desencriptando la contraseña que viene del programa.
        
        if decode == decode2:
            print("La contraseña ya existe, por favor intente con otra.")
            registro() #Trayendo el registro de nuevo.
    """
    
    print("Se insertaron los datos: ")
    print(nombre)
    print(apellido)
    print(usuario)
    print(conn)
    print(correo)
    
    #Línea SQL para insertar los datos en la BD.
    sql = "INSERT INTO datos_usuario VALUES (%s,%s,%s,%s,%s,%s)"

    if plan == 1: #Si el usuario eligió el número 1, entonces eligió el plan básico.
        print("Plan básico")
       
        plan1 = "Básico" #Insertando en letras el plan elegido.

        #Insertando los datos.
        cursor1.execute(sql,(nombre, apellido, usuario, conn, correo,plan1,))

        #Commit del query.
        conexion1.commit()

        #Cerrando la conexión.
        conexion1.close()

        basico(usuario) #Llamando al método de plan básico para que se registre el perfil de la persona.
                        #Se le pasa como parámetro el usuario para que cuando se inicie sesión, el sistema jale los datos que son.
        
    elif plan == 2: #Si el usuario eligió el número 2, entonces eligió el plan estándar.
        print("Plan estándar")

        plan2 = "Estándar" #Insertando en letras el plan elegido.

        #Insertando los datos.
        cursor1.execute(sql,(nombre, apellido, usuario, conn, correo,plan2,))
        
        #Commit del query.
        conexion1.commit()

        #Cerrando la conexión.
        conexion1.close()

        estandar(usuario) #Llamando al método de plan estándar para que se registren los perfiles de la persona.
                          #Se le pasa como parámetro el usuario para que cuando se inicie sesión, el sistema jale los datos que son.

    elif plan == 3: #Si el usuario eligió el número 3, entonces eligió el plan avanzado.
        print("Plan avanzado")

        plan3 = "Avanzado" #Insertando en letras el plan elegido.
        
        #Insertando los datos.
        cursor1.execute(sql,(nombre, apellido, usuario, conn, correo,plan3,))

        #Commit del query.
        conexion1.commit()

        #Cerrando la conexión.
        conexion1.close()

        avanzado(usuario) #Llamando al método de plan avanzado para que se registren los perfiles de la persona.
                          #Se le pasa como parámetro el usuario para que cuando se inicie sesión, el sistema jale los datos que son.

    """
    #Comprobando que la contraseña sea la misma.
    llave = 'UVG' #Llave para desencriptar.
    des = cryptocode.decrypt(conn, llave) #Desencriptando mensaje.
    print("Validando contraseña ", des)
    """