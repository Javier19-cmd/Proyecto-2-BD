from datos import * #Importando todos los datos de la base de datos.
import psycopg2 #Librería para abrir la base de datos.

#Menú principal para ver las opciones para ver los estados y cambios de los usuarios.
def ver_usuarios():
    while True:
        
        print("Bienvenido al menú para ver a los usuarios. \n")
        print("1. Dar de baja a un usuario")
        print("2. Cambiar dirección de correo de un usuario")
        print("3. Cambiar nombre de un usuario")
        print("4. Cambiar apellido de un usuario")
        print("5. Cambiar nombre de un usuario")
        print("6. Salir")

        try: 
            
            decision = int(input("¿Qué opción elije? "))

            if decision == 1: #Dar de baja a un usuario.
                dar_debaja() #Método para dar debaja a un usuario.
            elif decision == 2: #Cambiar dirección de correo de un usuario.
                print("Hola")
            elif decision == 3: #Cambiar nombre de un usuario.
                print("Hola") 
            elif decision == 4: #Cambiar apellido de un usuario.
                print("Hola")
            elif decision == 5: #Cambiar nombre de un usuario.
                print("Hola")
            elif decision == 6: #Salir de la pantalla.
                print("Saliendo....")
                break;
            else: #Opción no válida.
                print("Opción no válida.")

        except: #Opción no numérica elegida.
            print("Opción no numérica elegida")

#Método para poder debaja a los usuarios.
def dar_debaja():
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    usuario = input("Por favor escriba el usuario que desea dar debaja ")

    #SQL para eliminar datos de la persona.
    sql = "DELETE FROM datos_usuario WHERE usuario = %s"

    #SQL para eliminar perfiles de la persona.
    sql2 = "DELETE FROM perfiles WHERE usuario = %s"

    #Ejecutando los queries de eliminación. Primero se eliminó al usuario en la tabla de perfiles y luego en la tabla de datos_usuario.
    cursor1.execute(sql2, (usuario,)) #Eliminando persona de la tabla de perfiles.

    cursor1.execute(sql, (usuario,)) #Eliminando persona de la tabla de datos_usuario.

    #Haciendo commit de los queries.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

ver_usuarios()