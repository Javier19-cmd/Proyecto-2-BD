"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""

from datos import * #Importando todos los datos de la base de datos. 
from datetime import datetime #Librería para obtener la hora.
import psycopg2 #Importando la librería para implementar la base de datos.

def favoritos(perfil):

    while True:

        #Variable para la hora.
        now = datetime.now()
        #print(now)

        print("La búsqueda se puede hacer de la siguiente manera: \n")

        print("1) Nombre de película")
        print("2) Actores")
        print("3) Género")
        print("4) Director")
        print("5) Premio")
        print("6) Duración")
        print("7) Ver lista")
        print("8) Salir")


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

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                    #Query para buscar el nombre de las películas.
                    sql3 = "SELECT nombre, id FROM videos WHERE nombre = %s"
                    #Ejecutando el query de búsqueda. Este busca el nombre de la película.
                    cursor1.execute(sql3, (buscar,))
                    rows2=cursor1.fetchall()
                    print(rows2)

                    for row2 in rows2:
                        print("Nombre de la película: ", row2[0]) #Imprimiendo las películas del género.
                        print("Código de verificación: ", row2[1]) # Código de confirmación para meter la película al historial.


                        #Variable que contiene al nombre de la película.
                        buscar = input("Ingrese el nombre de la película que desea buscar: ")
                        confi = int(input("Ingrese el código de verificación que aparece debajo del nombre: "))
                        
                        #Query a usar para buscar con el nombre.
                        sql = "SELECT link FROM videos WHERE nombre = %s"

                        #Ejecutando el query de búsqueda.
                        cursor1.execute(sql, (buscar,))

                        rows=cursor1.fetchall()

                        #Imprimiendo el link de la película y el nombre.
                        for row in rows: 
                            #print(buscar)
                            print(row[0])

                            visto = 0
                            sql1 = "INSERT INTO favoritos VALUES (%s, %s, %s, %s, %s, %s)"
                            #Ejecutando el query de inserción.
                            cursor1.execute(sql1, (perfil, buscar, row[0], visto, now, confi,))

                            print("Enviando película la lista de favoritos")
               
                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

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

                #recomendacion_actor(buscar) #Recomendación de en base a los géneros.

                #Query a usar para buscar.
                sql = "SELECT v.nombre, v.link FROM videos v JOIN videos_actores va ON va.id_pelicula = v.id JOIN actores a on va.id = a.id WHERE a.nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    #print(buscar)
                    print(row[0])

                    #Query para buscar el nombre de las películas.
                    sql3 = "SELECT v.nombre, v.id FROM videos v JOIN videos_actores va ON va.id_pelicula = v.id JOIN actores a ON a.id = va.id WHERE a.nombre = %s"
                    #Ejecutando el query de búsqueda. Este busca el nombre de la película.
                    cursor1.execute(sql3, (buscar,))
                    rows2=cursor1.fetchall()

                    for row2 in rows2:
                        print("Nombre de la película: ", row2[0]) #Imprimiendo nombre de la película.
                        print("Código de verificación: ", row2[1]) #Imprimiendo el código de verificación de la película.

                        #Variable que contiene al nombre de la película.
                        buscar = input("Ingrese el nombre de la película que desea buscar: ")
                        confi = int(input("Ingrese el código de verificación de la película: "))

                        #Si en caso el código de verificación está malo, entonces se regresa al usuario de pantalla.
                        if confi != row2[1]:
                            print("Código inválido")
                            break

                        #Query a usar para buscar con el nombre.
                        sql = "SELECT link FROM videos WHERE nombre = %s"

                        #Ejecutando el query de búsqueda.
                        cursor1.execute(sql, (buscar,))

                        rows=cursor1.fetchall()

                        #Imprimiendo el link de la película y el nombre.
                        for row in rows: 
                            #print(buscar)
                            print(row[0])
                            visto = 0
                            sql1 = "INSERT INTO favoritos VALUES (%s, %s, %s, %s, %s, %s)"
                            #Ejecutando el query de búsqueda.
                            cursor1.execute(sql1, (perfil, buscar, row[0], visto, now, confi,))

                            print("Enviando película al historial")

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

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

                #recomendacion_genero(buscar) #Recomendación de en base a los géneros.

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE genero = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                    #Query para buscar el nombre de las películas.
                    sql3 = "SELECT nombre, id FROM videos WHERE genero = %s"
                    #Ejecutando el query de búsqueda. Este busca el nombre de la película.
                    cursor1.execute(sql3, (buscar,))
                    rows2=cursor1.fetchall()
                    print(rows2)

                    for row2 in rows2:
                        print("Nombre de la película: ", row2[0]) #Imprimiendo las películas del género.

                        #Variable que contiene al nombre de la película.
                        buscar = input("Ingrese el nombre de la película que desea buscar: ")
                        confi = int(input("Ingrese el código de verificación que aparece a un lado del nombre dentro de las listas: "))
                        

                        #Query a usar para buscar con el nombre.
                        sql = "SELECT link FROM videos WHERE nombre = %s"

                        #Ejecutando el query de búsqueda.
                        cursor1.execute(sql, (buscar,))

                        rows=cursor1.fetchall()

                        #Imprimiendo el link de la película y el nombre.
                        for row in rows: 
                            #print(buscar)
                            print(row[0])
                            visto = 0
                            sql1 = "INSERT INTO favoritos VALUES (%s, %s, %s, %s, %s, %s)"
                            #Ejecutando el query de búsqueda.
                            cursor1.execute(sql1, (perfil, buscar, row[0], visto, now, confi))

                            print("Enviando película al historial")

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

                #recomendacion_director(buscar) #Recomendación en base al director.

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE director = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    #print(buscar)
                    print(row[0])

                    #Query para buscar el nombre de las películas.
                    sql3 = "SELECT nombre, id FROM videos WHERE director = %s"
                    #Ejecutando el query de búsqueda. Este busca el nombre de la película.
                    cursor1.execute(sql3, (buscar,))
                    rows2=cursor1.fetchall()

                    for row2 in rows2:
                        print("Nombre de la película: ", row2[0]) #Imprimiendo las películas del género.
                        print("Código de verificación: ", row2[1]) #Código de verificación de la película.

                        #Variable que contiene al nombre de la película.
                        buscar = input("Ingrese el nombre de la película que desea buscar: ")
                        confi = int(input("Ingrese el código de verificación de la película: "))

                        if confi != row2[1]:
                            print("Código inválido")
                            break

                        #Query a usar para buscar con el nombre.
                        sql = "SELECT link FROM videos WHERE nombre = %s"

                        #Ejecutando el query de búsqueda.
                        cursor1.execute(sql, (buscar,))

                        rows=cursor1.fetchall()

                        #Imprimiendo el link de la película y el nombre.
                        for row in rows: 
                            print(buscar)
                            print(row[0])
                            visto = 0
                            sql1 = "INSERT INTO favoritos VALUES (%s, %s, %s, %s, %s, %s)"
                            #Ejecutando el query de búsqueda.
                            cursor1.execute(sql1, (perfil, buscar, row[0], visto, now, confi,))

                            print("Enviando película a la lista de favoritos")

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
                buscar = input("Ingrese el nombre del género que desea buscar: ")

                #recomendacion_premio(buscar) #Recomendación en base al premio.

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE premio = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(buscar)
                    print(row[0])

                    #Query para buscar el nombre de las películas.
                    sql3 = "SELECT nombre, id FROM videos WHERE premio = %s"
                    #Ejecutando el query de búsqueda. Este busca el nombre de la película.
                    cursor1.execute(sql3, (buscar,))
                    rows2=cursor1.fetchall()

                    for row2 in rows2:
                        print("Las películas del género son: ", row2[0]) #Imprimiendo las películas del género.
                        print("El código de verificación es: ", row2[1]) #Imprimiendo el código de verificiacón.

                        #Variable que contiene al nombre de la película.
                        buscar = input("Ingrese el nombre de la película que desea buscar: ")
                        confi = int(input("Ingrese el código de verificación de la película: "))
                        
                        #Si en caso el código de verificación está malo, entonces se regresa al usuario de pantalla.
                        if confi != row2[1]:
                            print("Código inválido")
                            break

                        #Query a usar para buscar con el nombre.
                        sql = "SELECT link FROM videos WHERE nombre = %s"

                        #Ejecutando el query de búsqueda.
                        cursor1.execute(sql, (buscar,))

                        rows=cursor1.fetchall()

                        #Imprimiendo el link de la película y el nombre.
                        for row in rows: 
                            #print(buscar)
                            print(row[0])
                            visto = 0
                            sql1 = "INSERT INTO favoritos VALUES (%s, %s, %s, %s, %s, %s)"
                            #Ejecutando el query de búsqueda.
                            cursor1.execute(sql1, (perfil, buscar, row[0], visto, now, confi,))

                            print("Enviando película a la lista de favoritos")

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 6: #Búsqueda por longitud. (Duración)

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
                buscar = input("Ingrese la longitud que desea buscar: ")

                #recomendacion_longitud(buscar) #Recomendación en base a la longitud.

                #Query a usar para buscar.
                sql = "SELECT link FROM videos WHERE duracion = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows:
                    print(row[0])

                    #Query para buscar el nombre de las películas.
                    sql3 = "SELECT nombre, id FROM videos WHERE duracion = %s"
                    #Ejecutando el query de búsqueda. Este busca el nombre de la película.
                    cursor1.execute(sql3, (buscar,))
                    rows2=cursor1.fetchall()

                    for row2 in rows2:
                        print("El nombre de la película es: ", row2[0]) #Imprimiendo las películas del género.
                        print("El código de verificación de la película es: ", row2[1])

                        #Variable que contiene al nombre de la película.
                        buscar = input("Ingrese el nombre de la película que desea buscar: ")
                        confi = int(input("Ingrese el código de verificación de la película: "))

                        #Si en caso el código de verificación está malo, entonces se regresa al usuario de pantalla.
                        if confi != row2[1]:
                            print("Código inválido")
                            break

                        #Query a usar para buscar con el nombre.
                        sql = "SELECT link FROM videos WHERE nombre = %s"

                        #Ejecutando el query de búsqueda.
                        cursor1.execute(sql, (buscar,))

                        rows=cursor1.fetchall()

                        #Imprimiendo el link de la película y el nombre.
                        for row in rows: 
                            #print(buscar)
                            print(row[0])
                            visto = 0
                            sql1 = "INSERT INTO favoritos VALUES (%s, %s, %s, %s, %s, %s)"
                            #Ejecutando el query de búsqueda.
                            cursor1.execute(sql1, (perfil, buscar, row[0], visto, now, confi,))

                            print("Enviando película a la lista de favoritos")

                #Insertando datos de búsqueda.    
                sql2 = "INSERT INTO busquedas VALUES (%s, %s, %s)"
                
                #Ejecutando el query de búsqueda.
                cursor1.execute(sql2, (perfil, buscar, now,))

                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
            
            elif eleccion == 7: #Ver lista de favoritos.
                #Conexión a la base de datos.
                conexion1 = psycopg2.connect(
                        host=host(), #Host de la base de datos.
                        user= user(), #Usuario de la base de datos.
                        password=passw(), #Contraseña de la base de datos.
                        database=BD(), #Base de datos que se usará.
                        port=port() #Puerto de la base de datos.
                )
                
                cursor1 = conexion1.cursor() #Cursor de la conexión.

                sql = "select nombre from favoritos f where perfil = %s" #Query que obtiene el nombre y el link de las películas que la persona mandó a favoritos.
                
                #Ejecutando el query de selección de favoritos.
                cursor1.execute(sql, (perfil,))

                rows=cursor1.fetchall()

                #Imprimiendo el link de la película.
                for row in rows: 
                    print(row[0])
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()


            elif eleccion == 8: #Salir.
                break; #Saliendo de la pantalla.
        except: 
            print("Error")