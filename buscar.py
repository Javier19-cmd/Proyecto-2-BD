from datos import * #Importando todos los datos de la base de datos. 
from datetime import datetime #Librería para obtener la hora.
import psycopg2 #Importando la librería para implementar la base de datos.

def buscar(perfil):

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #Variable para la hora.
    now = datetime.now()
    print("Hola")
    print(now)

    #Variable que contiene al nombre de la película.
    buscar = input("Ingrese el nombre de la película que desea buscar: ")

    #Query a usar para buscar.
    sql = "SELECT link FROM videos WHERE nombre = %s"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (buscar,))

    rows=cursor1.fetchall()

    #Imprimiendo el link de la película.
    for row in rows: 
        print(row[0])

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()


perfil = "Javier"
buscar(perfil)