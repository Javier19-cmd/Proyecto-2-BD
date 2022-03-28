from datos import * #Importando todos los datos de la base de datos. 
from datetime import datetime #Librería para obtener la hora.
import psycopg2 #Importando la librería para implementar la base de datos.

def buscar(perfil):

    while True:

        #Variable para la hora.
        now = datetime.now()
        print(now)

        print("La búsqueda se puede hacer de la siguiente manera: \n")

        print("1) Nombre de película")
        print("2) Actores")
        print("3) Género")
        print("4) Director")
        print("5) Premio")
        print("6) Duración")

        try: 
            eleccion = int(input("Cómo desea hacer su búsqueda "))

            if eleccion == 1: #Búsqueda por nombre de película.

                #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.
                
                #Variable que contiene al nombre de la película.
                buscar = input("Ingrese el nombre de la película que desea buscar: ")

                #Query a usar para buscar con el nombre.
                sql = "SELECT link FROM videos WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película y el nombre.
                for row in rows: 
                    print(buscar)
                    print(row[0])
                    

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 2: #Búsqueda por nombre de actor.
                
                #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.

                #Variable que contiene al nombre de la película.
                buscar = input("Ingrese el nombre del actor que desea buscar: ")

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE actor = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar,now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 3: #Búsquda por género.
            
            #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.

                #Variable que contiene al nombre de la película.
                buscar = input("Ingrese el nombre del género que desea buscar: ")

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE genero = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 4: #Búsqueda por director.
                
                #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.

                #Variable que contiene al nombre de la película.
                buscar = input("Ingrese el nombre del director que desea buscar: ")

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE director = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 5: #Búsqueda por premio.
                
                #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.

                #Variable que contiene al nombre de la película.
                buscar = input("Ingrese el nombre del premio que desea buscar: ")

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE premio = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows:
                    print(buscar) 
                    print(row[0])

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 6: #Búsqueda por fecha de estreno.

                #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.

                #Variable que contiene al nombre de la película.
                buscar = input("Ingrese la longitud de la película que desea buscar: ")

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE duracion = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
    

        except: #Esto es en caso de que la persona no eligió una opción no numérica.
            print("Elección no válida.")


perfil = "Javier"
buscar(perfil)