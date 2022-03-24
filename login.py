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

                normal() #Método para iniciar sesión con cuenta normal.

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
            print("Éxito")
<<<<<<< HEAD
=======
            
>>>>>>> parent of 4bd8dcd (buscando usuario y contraseña en la BD)
            #Verificando que la contraseña exista en la base de datos.
            #Buscando contraseña.
            sql2 = "SELECT contraseña FROM datos_usuario WHERE usuario = %s"

            cursor1.execute(sql2,(usuario,)) #Jalando contraseñas.
            rows2=cursor1.fetchall()
            #print(contra)
            for row1 in rows2:
                a = row1[0] #Guardando la contraseña en una variable.
                decode = cryptocode.decrypt(a, "UVG") #Desencriptando la varialbe.
<<<<<<< HEAD
                print(decode) #Imprimiendo la variable.
                if contraseña == decode: 
                    print("Éxito")
                else: #La contraseña no es igual.
                    print("La contraseña no es válida")
        else: #La contraseña no es igual.
            print("Usuario no encontrado")
=======
                #print(decode) #Imprimiendo la variable.
                if contraseña == decode: 
                    print("Éxito x2")
                    
        else: 
            #Se imprime un mensaje de error.
            print("Fracaso")
>>>>>>> parent of 4bd8dcd (buscando usuario y contraseña en la BD)
    

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



normal()