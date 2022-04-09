"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
#Importando todos los datos del perfil.
from datos import *
import psycopg2 #Librería para la base de datos.

#Método para ver el perfil.
def ver(usuario):
    while True:
        print("Bienvenido al menú para ver el perfil, ¿qué desea hacer? \n")
        print("1) Hacer downgrade")
        print("2) Salir")
        try: 
            eleccion = int(input("Elija su opción \n"))
            
            if eleccion == 1: #Hacer downgrade
                
                print("Opción de downgrade elegida \n")
                downgrade(usuario) #Opción de downgrade elegida.
            
            elif eleccion == 2: #Regresando a la pantalla anterior.
                print("Saliendo..... \n")
                break; 

            else: #Opción mayor o menor a uno
                
                print("Opción no válida")

        except: 
            print("Opción no numérica")

#Opción para hacer el downgrade
def downgrade(usuario):

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Opción de downgrade elegida \n")

    print(" Los planes a cambiar son: \n")

    print("1) Estándar")
    print("2) Gratis")

    try: 
        eleccion = int(input("¿Qué plan desea elegir? \n"))

        if eleccion == 1: #Si se eligió la opción 1, es porque el usuario quiere pasar de plan Avanzado a plan Estándar.

            sql = "UPDATE datos_usuario SET plan = 'Estándar' WHERE usuario = %s" #SQL para hacer update.

            #Trayendo los planes de la base de datos.
            cursor1.execute(sql, (usuario,))
            
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

            print("Plan actualizado")

        elif eleccion == 2: #Si el usuario eligió la opción 2, es porque el usuario quiere el plan gratis.
            
            sql2 = "UPDATE datos_usuario SET plan = 'Básico' WHERE usuario = %s" #SQL para hacer update.

            #Trayendo los planes de la base de datos.
            cursor1.execute(sql2, (usuario,))
            
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()

            print("Plan actualizado")
        else: #El usuario eligió una opción no válida.
            print("Opción no válida")
    except: #El usuario puso una opción no numérica.
        print("Opción no numérica elegida")