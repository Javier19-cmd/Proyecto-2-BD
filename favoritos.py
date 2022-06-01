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
                sql = "SELECT nombre FROM videos WHERE nombre ILIKE %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, ("%" + buscar + "%",))

                rows=cursor1.fetchall()

                #Imprimiendo los resultados de la búsqueda.
                lista = []

                for row in rows:
                    lista.append(row[0])
                
                print("\nResultados de la búsqueda: ")
                print(lista)

                #Pedir el nombre de la película.
                nombre = input("\nIngrese el nombre de la película que desea ver: ")

                #Revisar si la película existe.
                if nombre in lista:
                        
                    #Query para obtener el id de la película.
                    sql = "SELECT nombre, link, id FROM videos WHERE nombre = %s"

                    #Ejecutando el query.
                    cursor1.execute(sql, (nombre,))

                    rows=cursor1.fetchall()


                    #Imprimiendo el id de la película.
                    for row in rows:
                        print("\nEl nombre de la película es: " + str(row[0]))
                        print("\nEl link de la película es: " + str(row[1]))
                        print("\nEl id de la película es: " + str(row[2]))

                        #Variables que mandarán los datos al historial.
                        perf = perfil
                        nombres = row[0]
                        links = row[1]
                        visto = 0
                        #Now
                        ahorita = datetime.now() 
                        ide = row[2]

                        print(perf)
                        print(nombres)
                        print(links)
                        print(visto)
                        print(ahorita)
                        print(ide)

                        #Insertando los datos en la base de datos.
                        sql = "INSERT INTO favoritos (perfil, nombre, link, visto, tiempo, id_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"

                        #Ejecutando el query para insertar en el historial.
                        cursor1.execute(sql, (perf, nombres, links, visto, ahorita, ide,))
               
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
                sql = "SELECT v.nombre, v.link FROM videos v JOIN videos_actores va ON va.id_pelicula = v.id JOIN actores a on va.id_actor = a.id WHERE a.nombre ILIKE %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, ("%" + buscar + "%",))

                rows=cursor1.fetchall()

                #Lista para guardar las películas del actor.
                listas = []

                for a in rows:
                    listas.append(a[0])
                
                #Imprimiendo los resultados de la búsqueda.
                print(listas)

                #Pedir el nombre de la película.
                nombress = input("\nIngrese el nombre de la película que desea buscar: ")

                #Seleccionar la película.
                if nombress in listas:
                    #Query para obtener el id de la película.
                    sqla = "SELECT nombre, link, id FROM videos WHERE nombre = %s"

                    #Ejecutando el query.
                    cursor1.execute(sqla, (nombress,))

                    rows=cursor1.fetchall()


                    #Imprimiendo el id de la película.
                    for row in rows:
                        print("\nEl nombre de la película es: " + str(row[0]))
                        print("\nEl link de la película es: " + str(row[1]))
                        print("\nEl id de la película es: " + str(row[2]))

                        #Variables que mandarán los datos al historial.
                        perfi = perfil
                        nombresss = row[0]
                        linkss = row[1]
                        visto = 0
                        #Now
                        ahoritas = datetime.now() 
                        ides = row[2]

                        print(perfi)
                        print(nombresss)
                        print(linkss)
                        print(visto)
                        print(ahoritas)
                        print(ides)

                        #Insertando los datos en la base de datos.
                        sql = "INSERT INTO favoritos (perfil, nombre, link, visto, tiempo, id_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"

                        #Ejecutando el query para insertar en el historial.
                        cursor1.execute(sql, (perfi, nombresss, linkss, visto, ahoritas, ides,))

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
                sql = "SELECT nombre FROM videos WHERE genero ILIKE %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, (buscar,))

                rows=cursor1.fetchall()

                #Imprimiendo los resultados de la búsqueda.
                lista = []

                for row in rows:
                    lista.append(row[0])
                
                print("\nResultados de la búsqueda: ")
                print(lista)

                #Pedir el nombre de la película.
                nombre = input("\nIngrese el nombre de la película que desea ver: ")

                #Revisar si la película existe.
                if nombre in lista:
                        
                    #Query para obtener el id de la película.
                    sql = "SELECT nombre, link, id FROM videos WHERE nombre = %s"
    
                    #Ejecutando el query.
                    cursor1.execute(sql, (nombre,))
    
                    rows=cursor1.fetchall()


                    #Imprimiendo el id de la película.
                    for row in rows:
                        print("\nEl nombre de la película es: " + str(row[0]))
                        print("\nEl link de la película es: " + str(row[1]))
                        print("\nEl id de la película es: " + str(row[2]))

                        #Variables que mandarán los datos al historial.
                        perf = perfil
                        nombres = row[0]
                        links = row[1]
                        visto = 0
                        #Now
                        ahorita = datetime.now() 
                        ide = row[2]

                        print(perf)
                        print(nombres)
                        print(links)
                        print(visto)
                        print(ahorita)
                        print(ide)

                        #Insertando los datos en la base de datos.
                        sql = "INSERT INTO favoritos (perfil, nombre, link, visto, tiempo, id_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"

                        #Ejecutando el query para insertar en el historial.
                        cursor1.execute(sql, (perf, nombres, links, visto, ahorita, ide,))

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
                sql = "SELECT nombre FROM videos WHERE director ILIKE %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, ("%" + buscar + "%",))

                rows=cursor1.fetchall()

                #Imprimiendo los resultados de la búsqueda.
                lista = []

                for row in rows:
                    lista.append(row[0])
                
                print("\nResultados de la búsqueda: ")
                print(lista)

                #Pedir el nombre de la película.
                nombre = input("\nIngrese el nombre de la película que desea ver: ")

                #Revisar si la película existe.
                if nombre in lista:
                        
                    #Query para obtener el id de la película.
                    sql = "SELECT nombre, link, id FROM videos WHERE nombre = %s"
    
                    #Ejecutando el query.
                    cursor1.execute(sql, (nombre,))
    
                    rows=cursor1.fetchall()

    
                    #Imprimiendo el id de la película.
                    for row in rows:
                        print("\nEl nombre de la película es: " + str(row[0]))
                        print("\nEl link de la película es: " + str(row[1]))
                        print("\nEl id de la película es: " + str(row[2]))

                        #Variables que mandarán los datos al historial.
                        perf = perfil
                        nombres = row[0]
                        links = row[1]
                        visto = 0
                        #Now
                        ahorita = datetime.now() 
                        ide = row[2]

                        print(perf)
                        print(nombres)
                        print(links)
                        print(visto)
                        print(ahorita)
                        print(ide)

                        #Insertando los datos en la base de datos.
                        sql = "INSERT INTO favoritos (perfil, nombre, link, visto, tiempo, id_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"

                        #Ejecutando el query para insertar en el historial.
                        cursor1.execute(sql, (perf, nombres, links, visto, ahorita, ide,))

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

                #recomendacion_premio(buscar) #Recomendación en base al premio.

                #Query a usar para buscar.
                sql = "SELECT nombre FROM videos WHERE premio ILIKE %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, ("%" + buscar + "%",))

                rows=cursor1.fetchall()

                #Imprimiendo los resultados de la búsqueda.
                lista = []

                for row in rows:
                    lista.append(row[0])
                
                print("\nResultados de la búsqueda: ")
                print(lista)

                #Pedir el nombre de la película.
                nombre = input("\nIngrese el nombre de la película que desea ver: ")

                #Revisar si la película existe.
                if nombre in lista:
                    
                    #Query para obtener el id de la película.
                    sql = "SELECT nombre, link, id FROM videos WHERE nombre = %s"
    
                    #Ejecutando el query.
                    cursor1.execute(sql, (nombre,))
    
                    rows=cursor1.fetchall()

    
                    #Imprimiendo el id de la película.
                    for row in rows:
                        print("\nEl nombre de la película es: " + str(row[0]))
                        print("\nEl link de la película es: " + str(row[1]))
                        print("\nEl id de la película es: " + str(row[2]))

                        #Variables que mandarán los datos al historial.
                        perf = perfil
                        nombres = row[0]
                        links = row[1]
                        visto = 0
                        #Now
                        ahorita = datetime.now() 
                        ide = row[2]

                        print(perf)
                        print(nombres)
                        print(links)
                        print(visto)
                        print(ahorita)
                        print(ide)

                        #Insertando los datos en la base de datos.
                        sql = "INSERT INTO favoritos (perfil, nombre, link, visto, tiempo, id_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"

                        #Ejecutando el query para insertar en el historial.
                        cursor1.execute(sql, (perf, nombres, links, visto, ahorita, ide,))

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
                sql = "SELECT nombre FROM videos WHERE duracion ILIKE %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql, ("%" + buscar + "%",))

                rows=cursor1.fetchall()

                #Imprimiendo los resultados de la búsqueda.
                lista = []

                for row in rows:
                    lista.append(row[0])
                
                print("\nResultados de la búsqueda: ")
                print(lista)

                #Pedir el nombre de la película.
                nombre = input("\nIngrese el nombre de la película que desea ver: ")

                #Revisar si la película existe.
                if nombre in lista:
                        
                    #Query para obtener el id de la película.
                    sql = "SELECT nombre, link, id FROM videos WHERE nombre = %s"
    
                    #Ejecutando el query.
                    cursor1.execute(sql, (nombre,))
    
                    rows=cursor1.fetchall()

    
                    #Imprimiendo el id de la película.
                    for row in rows:
                        print("\nEl nombre de la película es: " + str(row[0]))
                        print("\nEl link de la película es: " + str(row[1]))
                        print("\nEl id de la película es: " + str(row[2]))

                        #Variables que mandarán los datos al historial.
                        perf = perfil
                        nombres = row[0]
                        links = row[1]
                        visto = 0
                        #Now
                        ahorita = datetime.now() 
                        ide = row[2]

                        print(perf)
                        print(nombres)
                        print(links)
                        print(visto)
                        print(ahorita)
                        print(ide)

                        #Insertando los datos en la base de datos.
                        sql = "INSERT INTO favoritos (perfil, nombre, link, visto, tiempo, id_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"

                        #Ejecutando el query para insertar en el historial.
                        cursor1.execute(sql, (perf, nombres, links, visto, ahorita, ide,))

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

                sql = "select distinct nombre from favoritos f where perfil = %s" #Query que obtiene el nombre y el link de las películas que la persona mandó a favoritos.
                
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

#favoritos("Javier")