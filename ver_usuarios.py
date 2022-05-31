"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
from datos import * #Importando todos los datos de la base de datos.
import psycopg2 #Librería para abrir la base de datos.
from datetime import datetime #Librería para obtener la hora.

#Menú principal para ver las opciones para ver los estados y cambios de los usuarios.
def ver_usuarios():
    while True:
        
        print("Bienvenido al menú para ver a los usuarios. \n")
        print("1. Dar de baja a un usuario")
        print("2. Cambiar dirección de correo de un usuario")
        print("3. Cambiar nombre de un usuario")
        print("4. Cambiar apellido de un usuario")
        print("5. Salir")

        try: 
            
            decision = int(input("¿Qué opción elije? "))

            if decision == 1: #Dar de baja a un usuario.

                dar_debaja() #Método para dar debaja a un usuario.
            
            elif decision == 2: #Cambiar dirección de correo de un usuario.
             
                cambiar_correo() #Método para cambiar el correo de la persona.
            
            elif decision == 3: #Cambiar nombre de un usuario.
            
                cambiar_nombre() #Método para cambiar nombre de la persona.
            
            elif decision == 4: #Cambiar apellido de un usuario.
            
                cambiar_apellido() #Método que cambia el apellido de la persona.
            
            elif decision == 5: #Salir de la pantalla.
            
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
    #sql2 = "DELETE FROM perfiles WHERE usuario = %s"

    #Ejecutando los queries de eliminación. Primero se eliminó al usuario en la tabla de perfiles y luego en la tabla de datos_usuario.
    #cursor1.execute(sql2, (usuario,)) #Eliminando persona de la tabla de perfiles.

    cursor1.execute(sql, (usuario,)) #Eliminando persona de la tabla de datos_usuario.

    #Haciendo commit de los queries.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

    print("Usuario dado de baja")

    #mod1() #Método para meter las modficiaciones que hizo el administrador.

#Método para cambiar el correo de las personas.
def cambiar_correo():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Para el correo de la persona, a continuación escriba su usuario")
        
    #Pidiendo el usuario de la persona.
    usuario = input("Ingrese usuario de la persona ")

    #Query a usar para buscar con el nombre.
    sql = "SELECT usuario FROM datos_usuario WHERE usuario = %s"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (usuario,))

    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 

        print(row[0])
        
        if usuario == row[0]:
            
            act = input("Ingrese el nuevo correo de la persona: ")

            sql1 = "UPDATE datos_usuario SET correo = %s WHERE usuario = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql1, (act, usuario,))
            
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
            
            print("Correo actualizado \n")

            #mod2() #Método para meter las modficiaciones que hizo el administrador.

            break;

#Método para cambiar el nombre de la persona.
def cambiar_nombre():
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Para el nombre de la persona, a continuación escriba su usuario")
        
    #Pidiendo el usuario de la persona.
    usuario = input("Ingrese usuario de la persona ")

    #Query a usar para buscar con el nombre.
    sql = "SELECT usuario FROM datos_usuario WHERE usuario = %s"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (usuario,))

    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 

        print(row[0])
        
        if usuario == row[0]:
            
            act = input("Ingrese el nuevo nombre de la persona: ")

            sql1 = "UPDATE datos_usuario SET nombre = %s WHERE usuario = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql1, (act, usuario,))
            
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
            
            print("Nombre actualizado \n")

            #mod3() #Método para registrar la modificación del administrador.

            break;

#Método para cambiar el apellido de la persona.
def cambiar_apellido():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Para el apellido de la persona, a continuación escriba su usuario")
        
    #Pidiendo el usuario de la persona.
    usuario = input("Ingrese usuario de la persona ")

    #Query a usar para buscar con el nombre.
    sql = "SELECT usuario FROM datos_usuario WHERE usuario = %s"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (usuario,))

    rows=cursor1.fetchall()

    #Imprimiendo el apellido de la persona.
    for row in rows: 

        print(row[0])
        
        if usuario == row[0]:
            
            act = input("Ingrese el nuevo apellido de la persona: ")

            sql1 = "UPDATE datos_usuario SET apellido = %s WHERE usuario = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql1, (act, usuario,))
            
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
            
            print("Apellido actualizado \n")

            #mod4() #Método para registrar la modificación del administrador.

            break;

"""
def mod1(): #Insertando la modificación que se hizo. En este caso borrar cuenta.
    
        #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    now = datetime.now() #Momento actual en donde se está eliminando al usuario.

    modificacion = "Dar debaja" #Detalle de la modificación.

    us = input("Escriba su usuario de administrador: ") #Pidiendo el usuario de administrador.

    sql3 = "INSERT INTO modificaciones_administradores VALUES (%s, %s, %s)"

    cursor1.execute(sql3, (us, modificacion, now,))

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

def mod2(): #Insertando la modificación que se hizo. En este caso modificiacón de correo.
    
        #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    now = datetime.now() #Momento actual en donde se está eliminando al usuario.

    modificacion = "Modificación de correo" #Detalle de la modificación.

    us = input("Escriba su usuario de administrador: ") #Pidiendo el usuario de administrador.

    sql3 = "INSERT INTO modificaciones_administradores VALUES (%s, %s, %s)"

    cursor1.execute(sql3, (us, modificacion, now,))

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

def mod3(): #Insertando la modificación que se hizo. En este caso modificiacón del nombre.

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    now = datetime.now() #Momento actual en donde se está eliminando al usuario.

    modificacion = "Cambio del nombre" #Detalle de la modificación.

    us = input("Escriba su usuario de administrador: ") #Pidiendo el usuario de administrador.

    sql3 = "INSERT INTO modificaciones_administradores VALUES (%s, %s, %s)"

    cursor1.execute(sql3, (us, modificacion, now,))

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

def mod4(): #Insertando la modificación que se hizo. En este caso modificiacón del apellido.

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    now = datetime.now() #Momento actual en donde se está eliminando al usuario.

    modificacion = "Cambio del apellido" #Detalle de la modificación.

    us = input("Escriba su usuario de administrador: ") #Pidiendo el usuario de administrador.

    sql3 = "INSERT INTO modificaciones_administradores VALUES (%s, %s, %s)"

    cursor1.execute(sql3, (us, modificacion, now,))

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()
"""