from datos import * #Importando los datos de la BD.
import psycopg2     #Importando la librería de la BD.
import random


def va(): 

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
        host=host(), #Host de la base de datos.
        user= user(), #Usuario de la base de datos.
        password=passw(), #Contraseña de la base de datos.
        database=BD(), #Base de datos que se usará.
        port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #SQL para meter los datos aleatorios.
    sql = "INSERT INTO videos_actores(id_pelicula, id_actor) VALUES (%s, %s)"

    #Cantidad de veces que se meterán a los actores en videos.
    cantidad = 150

    for i in range(cantidad):
        
        #Selección random de una película.
        sql1 = "SELECT RANDOM() AS orden, id FROM videos ORDER BY orden limit 1"

        cursor1.execute(sql1) #Corriendo el sql.

        a = cursor1.fetchall() #Guardando los datos obtenidos.

        print(a) #Trayendo la tupla de las películas. Esto es una lista de dos dimensiones.

        listaP = [a[0][1]] #Lista de las películas aleatorias a ver.

        print(listaP[0]) #Imprimiendo solo el ID.

        id = listaP[0] #Guardando el id en una variable.

        #Seleccionando perfil aleatorio de prueba.
        sql2 = "SELECT RANDOM() AS orden, id FROM actores ORDER BY orden limit 1"
        
        cursor1.execute(sql2) #Corriendo el sql.
        
        b = cursor1.fetchall() #Trayendo actores.

        print(b) #Imprimiendo la tupla que trae al usuario. Es un listado de dos dimensiones. 

        listaA = [b[0][1]] #Se guarda en la listaU solamente el nombre del perfil que se quiere meter a la BD.
        
        print("Actor ", listaA[0]) #Imprimiendo al perfil que verá aleatoriamente la película.

        actor = listaA[0] #Obteniendo el perfil que verá las películas.

        cursor1.execute(sql, (id, actor,))

    conexion1.commit()

    conexion1.close()

va()