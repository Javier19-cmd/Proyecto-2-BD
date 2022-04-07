from datos import * #Importando los datos de la BD.
import psycopg2 #Importando módulo para conectar a PostgreSQL

#Recomendación del nombre.
def recomendacion_nombre(nombre):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    sql = "SELECT genero FROM videos WHERE nombre = %s"

    cursor1.execute(sql, (nombre,))
    rows2=cursor1.fetchall()

    #Imprimiendo anuncio.
    for row2 in rows2: 
        print("Los géneros que te recomendamos son: ", row2[0])
        print("\n")

#Recomendación del actor.
def recomendacion_actor(actor):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    sql = "SELECT v.nombre FROM videos v JOIN videos_actores va ON va.id_pelicula = v.id WHERE va.nombre = %s"

    cursor1.execute(sql, (actor,))
    rows2=cursor1.fetchall()
    
    #Imprimiendo anuncio.
    for row2 in rows2: 
        print("Las películas recomendadas son: ", row2[0])
        print("\n")

#Recomendación del género.
def recomendacion_genero(genero):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    sql = "SELECT nombre FROM videos WHERE genero = %s"

    cursor1.execute(sql, (genero,))
    rows2=cursor1.fetchall()

    #Imprimiendo anuncio.
    for row2 in rows2: 
        print("Las películas recomendadas son: ", row2[0])
        print("\n")


#Recomendación del nombre.
def recomendacion_director(director):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    sql = "SELECT genero FROM videos WHERE director = %s"

    cursor1.execute(sql, (director,))
    rows2=cursor1.fetchall()

    #Imprimiendo anuncio.
    for row2 in rows2: 
        print("Los géneros que te recomendamos son: ", row2[0])
        print("\n")

#Recomendación del nombre.
def recomendacion_longitud(duracion):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    sql = "SELECT genero FROM videos WHERE duracion = %s"

    cursor1.execute(sql, (duracion,))
    rows2=cursor1.fetchall()

    #Imprimiendo anuncio.
    for row2 in rows2: 
        print("Los géneros que te recomendamos son: ", row2[0])
        print("\n")

#Recomendación del nombre.
def recomendacion_premio(premio):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    sql = "SELECT genero FROM videos WHERE premio = %s"

    cursor1.execute(sql, (premio,))
    rows2=cursor1.fetchall()

    #Imprimiendo anuncio.
    for row2 in rows2: 
        print("Los géneros que te recomendamos son: ", row2[0])
        print("\n")