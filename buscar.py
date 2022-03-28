from datos import * #Importando todos los datos de la base de datos. 
from datetime import datetime #Librería para obtener la hora.
import psycopg2 #Importando la librería para implementar la base de datos.

def buscar(perfil):

    #Variable para la hora.
    now = datetime.now()
    print(now)

    print("La búsqueda se puede hacer de la siguiente manera: \n")

    print("1) Por nombre de película")
    print("2) Por actores")
    print("3) Género")
    print("4) Director")
    print("5) Premio")
    print("6) Fecha_estreno")

    try: 
        eleccion = int(input("Cómo desea hacer su búsqueda "))

        if eleccion == 1: 
            #Conexión a la base de datos.
            conexion1 = psycopg2.connect(
                    host=host(), #Host de la base de datos.
                    user= user(), #Usuario de la base de datos.
                    password=passw(), #Contraseña de la base de datos.
                    database=BD(), #Base de datos que se usará.
                    port=port() #Puerto de la base de datos.
            )
            
            cursor1 = conexion1.cursor() #Cursor de la conexión.
                
            #Búsqueda por nombre de película.

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

            #Insertando datos de búsqueda.    
            sql2 = "INSERT INTO busquedas VALUES (%s, %s)"
            
            #Ejecutando el query de búsqueda.
            cursor1.execute(sql2, (perfil, buscar,))

            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()


    except:
        print("Elección no válida.")




perfil = "Javier"
buscar(perfil)