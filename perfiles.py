#Importando los datos de la BD.
from datos import *
#Librería para la base de datos.
import psycopg2 


#Opciones para registrar a los perfiles del sistema.

def basico(usuario):

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #El usuario solo puede tener como máximo a un usuario. 
    perfil = input("Ingrese el nombre del perfil: ")

    #Query para insertar el perfil de la persona que eligió el plan básico.
    sql = "INSERT INTO perfiles VALUES (%s, %s)"

    #Insertando los datos en la base de datos.
    cursor1.execute(sql,(usuario,perfil,))

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

def estandar(usuario): #Se insertarán los perfiles elegidos más el usuario.
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    while True:
        #El usuario puede elegir como máximo a cuatro perfiles.
        decision = int(input("¿Cuántos perfiles desea tener? "))

        if decision == 1: 
            #Insertar el usuario y el perfil.
            #El usuario eligió a dos perfiles.
            perfil = input("Ingrese el nombre del usuario: ")
            
            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

        elif decision == 2: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a dos perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
        
        elif decision == 3: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a tres perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
        
        elif decision == 4: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a cuatro perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))
            cursor1.execute(sql,(usuario,perfil4,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

        else: 
            #Se eligieron más perfiles.
            print("No se pueden elegir más perfiles.")


def avanzado(usuario):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #El usuario puede elegir como máximo a ocho perfiles.
    while True:
        #El usuario puede elegir como máximo a cuatro perfiles.
        decision = int(input("¿Cuántos perfiles desea tener? "))

        if decision == 1: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a dos perfiles.
            perfil = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

        elif decision == 2: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a dos perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
        
        elif decision == 3: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a tres perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

        
        elif decision == 4: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a cuatro perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            
            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))
            cursor1.execute(sql,(usuario,perfil4,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

        elif decision == 5: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a cinco perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")

            #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))
            cursor1.execute(sql,(usuario,perfil4,))
            cursor1.execute(sql,(usuario,perfil5,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
        
        elif decision == 6: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a seis perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
            perfil6 = input("Ingrese el nombre del usuario: ")

           #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))
            cursor1.execute(sql,(usuario,perfil4,))
            cursor1.execute(sql,(usuario,perfil5,))
            cursor1.execute(sql,(usuario,perfil6,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

        elif decision == 7: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a siete perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
            perfil6 = input("Ingrese el nombre del usuario: ")
            perfil7 = input("Ingrese el nombre del usuario: ")

           #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))
            cursor1.execute(sql,(usuario,perfil4,))
            cursor1.execute(sql,(usuario,perfil5,))
            cursor1.execute(sql,(usuario,perfil6,))
            cursor1.execute(sql,(usuario,perfil7,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
        
        elif decision == 8: 
            #Insertar el usuario y los perfiles.
            #El usuario eligió a ocho perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
            perfil6 = input("Ingrese el nombre del usuario: ")
            perfil7 = input("Ingrese el nombre del usuario: ")
            perfil8 = input("Ingrese el nombre del usuario: ")

           #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
            sql = "INSERT INTO perfiles VALUES (%s, %s)"

            #Insertando los datos en la base de datos.
            cursor1.execute(sql,(usuario,perfil1,))
            cursor1.execute(sql,(usuario,perfil2,))
            cursor1.execute(sql,(usuario,perfil3,))
            cursor1.execute(sql,(usuario,perfil4,))
            cursor1.execute(sql,(usuario,perfil5,))
            cursor1.execute(sql,(usuario,perfil6,))
            cursor1.execute(sql,(usuario,perfil7,))
            cursor1.execute(sql,(usuario,perfil8,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
        
        else: 
            #Se puso una cantidad que no se puede.
            print("Cantidad no válida")
