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

    #Seleccionando los perfiles de la tabla.
    #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
    cursor1.execute("SELECT perfil FROM perfiles")
    rows=cursor1.fetchall()
    for row in rows:
        #print(row[0])
        if perfil == row[0]:
            print("Perfil existente, favor regresar a ingresar bien los datos")
            basico(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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
        
        #Try-catch para evitar que el usuario no meta una opción no numérica.
        try: 
            if decision == 1: 
                #Insertar el usuario y el perfil.
                #El usuario eligió a dos perfiles.
                perfil = input("Ingrese el nombre del usuario: ")

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil == row[0]:
                        print("Perfil existente, favor intente con otro tipo de usuario")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfiles existentes, favor intente con otros usuarios")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil4 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        estandar(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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
        
        except: #Opción no numérica.
            print("Opción no válida.")
        
        break; #Regresando a la página de inicio.


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

        #Try-catch para evitar que el usuario no elija una opción no numérica.
        try: 
            if decision == 1: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a dos perfiles.
                perfil = input("Ingrese el nombre del usuario: ")

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil4 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil4 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil5 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil4 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil5 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil6 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil4 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil5 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil6 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil7 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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

               #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil1 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil2 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil3 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil4 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.
                
                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil5 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil6 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil7 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

                #Seleccionando los perfiles de la tabla.
                #Verificando que el perfil ingresado no exista en la tabla. En caso de que exista, entonces se manda al cliente a registrar bien otra vez los perfiles.
                cursor1.execute("SELECT perfil FROM perfiles")
                rows=cursor1.fetchall()
                for row in rows:
                    #print(row[0])
                    if perfil8 == row[0]:
                        print("Perfil existente, favor regresar a ingresar bien los datos")
                        avanzado(usuario) #Si el usuario ya existe, entonces se regresa a poner bien los datos otra vez.

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
        
        except: #Opción no numérica. 
            print("Opción no válida")
        
        break; #Regresando a la página de inicio.

