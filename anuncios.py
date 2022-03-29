from datos import * #Importando los datos de la BD.
import psycopg2 #Importando librería que conecta con postgres.

#Archivo que se va a encargar de generar los anuncios de la plataforma.
def anuncios ():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Hola")

anuncios()