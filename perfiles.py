"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
#Importando los datos de la BD.
from datos import *
#Librería para la base de datos.
import psycopg2 
from conexion import *


#Opciones para registrar a los perfiles del sistema.

def basico(usuario):

    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #El usuario solo puede tener como máximo a un usuario. 
    perfil = input("Ingrese el nombre del perfil: ")

    #Query para insertar el perfil de la persona que eligió el plan básico.
    sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

    #Indicando que el perfil no ha ingresado.
    ingreso = 0

    #Insertando los datos en la base de datos.
    cursor1.execute(sql,(usuario,perfil, ingreso,))

    #Commit del query.
    conexion1.commit()

def estandar(usuario): #Se insertarán los perfiles elegidos más el usuario.
    
    #Conexión a la base de datos.
    conexion1 = getConnection()

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
                
                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"
                
                #Indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil, ingreso,))

                #Commit del query.
                conexion1.commit()

            elif decision == 2: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a dos perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"
                
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))

                #Commit del query.
                conexion1.commit()
            
            elif decision == 3: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a tres perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")
                perfil3 = input("Ingrese el nombre del usuario: ")

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2,ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))

                #Commit del query.
                conexion1.commit()
            
            elif decision == 4: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a cuatro perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")
                perfil3 = input("Ingrese el nombre del usuario: ")
                perfil4 = input("Ingrese el nombre del usuario: ")

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Indicando que el usuario no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))
                cursor1.execute(sql,(usuario,perfil4, ingreso,))

                #Commit del query.
                conexion1.commit()

            else: 
                #Se eligieron más perfiles.
                print("No se pueden elegir más perfiles.")
        
        except: #Opción no numérica.
            print("Opción no válida.")
        
        break; #Regresando a la página de inicio.


def avanzado(usuario):
    #Conexión a la base de datos.
    conexion1 = getConnection()

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

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"


                #Indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil, ingreso,))

                #Commit del query.
                conexion1.commit()

            elif decision == 2: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a dos perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")

                #Indicando que el perfil no ha ingresado.
                ingreso = 0

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))

                #Commit del query.
                conexion1.commit()
            
            elif decision == 3: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a tres perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")
                perfil3 = input("Ingrese el nombre del usuario: ")

                #Indicando que el perfil no ha ingresado
                ingreso = 0

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))

                #Commit del query.
                conexion1.commit()

            
            elif decision == 4: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a cuatro perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")
                perfil3 = input("Ingrese el nombre del usuario: ")
                perfil4 = input("Ingrese el nombre del usuario: ")
                
                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))
                cursor1.execute(sql,(usuario,perfil4, ingreso,))

                #Commit del query.
                conexion1.commit()

            elif decision == 5: 
                #Insertar el usuario y los perfiles.
                #El usuario eligió a cinco perfiles.
                perfil1 = input("Ingrese el nombre del usuario: ")
                perfil2 = input("Ingrese el nombre del usuario: ")
                perfil3 = input("Ingrese el nombre del usuario: ")
                perfil4 = input("Ingrese el nombre del usuario: ")
                perfil5 = input("Ingrese el nombre del usuario: ")

                #Query para insertar el perfil de la persona que eligió el plan estándar con 1 usuario.
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))
                cursor1.execute(sql,(usuario,perfil4, ingreso,))
                cursor1.execute(sql,(usuario,perfil5, ingreso,))

                #Commit del query.
                conexion1.commit()
            
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
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))
                cursor1.execute(sql,(usuario,perfil4, ingreso,))
                cursor1.execute(sql,(usuario,perfil5, ingreso,))
                cursor1.execute(sql,(usuario,perfil6, ingreso,))

                #Commit del query.
                conexion1.commit()

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
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #Indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))
                cursor1.execute(sql,(usuario,perfil4, ingreso,))
                cursor1.execute(sql,(usuario,perfil5, ingreso,))
                cursor1.execute(sql,(usuario,perfil6, ingreso,))
                cursor1.execute(sql,(usuario,perfil7, ingreso,))

                #Commit del query.
                conexion1.commit()
            
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
                sql = "INSERT INTO perfiles VALUES (%s, %s, %s)"

                #indicando que el perfil no ha ingresado.
                ingreso = 0

                #Insertando los datos en la base de datos.
                cursor1.execute(sql,(usuario,perfil1, ingreso,))
                cursor1.execute(sql,(usuario,perfil2, ingreso,))
                cursor1.execute(sql,(usuario,perfil3, ingreso,))
                cursor1.execute(sql,(usuario,perfil4, ingreso,))
                cursor1.execute(sql,(usuario,perfil5, ingreso,))
                cursor1.execute(sql,(usuario,perfil6, ingreso,))
                cursor1.execute(sql,(usuario,perfil7, ingreso,))
                cursor1.execute(sql,(usuario,perfil8, ingreso,))

                #Commit del query.
                conexion1.commit()
            
            else: 
                #Se puso una cantidad que no se puede.
                print("Cantidad no válida")
        
        except: #Opción no numérica. 
            print("Opción no válida")
        
        break; #Regresando a la página de inicio.

