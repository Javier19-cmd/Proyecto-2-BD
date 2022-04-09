"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
#Archivo que modifica el contenido que ven los usuarios.
from datos import * #Importando los datos de la base de datos.
import psycopg2 #Librería para abrir la base de datos.

#Método que modifica el contenido.
def modificar_contenido():
    while True:

        print("Bienvenido al menú que modica el contenido de la plataforma. \n")
        print("Las opciones disponibles son: \n")
        print("1. Agregar contenido")
        print("2. Modificar")
        print("3. Eliminar contenido")
        print("4. Salir")

        try: 
            eleccion = int(input("¿Qué opción desea elegir? "))

            if eleccion == 1: #Agregar contenido a la plataforma.
                print("Opción para agregar contenido elegida")
                agregar_contenido() #Llamando el método que agrega contenido.
            elif eleccion == 2: #Opción de modificar contenido.
                print("Opción de modificar contenido elegido")
                modificar_contenido() #Opción para modificar el contenido de la base de datos.
            elif eleccion == 3: #Opción para eliminar contenido.
                print("Opción para eliminar contenido elegido")
                eliminar_contenido() #Opción para eliminar contenido.
            elif eleccion == 4: #Opción para salir. 
                print("Saliendo")
                break;
            else: #Opción no válida.
                print("Opción no válida")

        except: 
            print("Opción no válida")

#Método para agregar contenido.        
def agregar_contenido():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    """
    Actualizar:
     1. Nombre
     2. Actores
     3. Género
     4. Director
     5. Premio
     6. Fecha_streno
     7. Link 
     8. Duración (en minutos) 
    """

    #Pidiendo datos.
    nombre = input("Ingrese el nombre de la película ")
    actores = input("Ingrese a los actores ")
    genero = input("Ingrese el género ")
    director = input("Ingrese el nombre del director ")
    premio = input("Ingrese un premio de la película ")
    fecha = input("Ingrese la fecha de estreno ")
    link = input("Ingrese el link de la película ")
    duracion = input("Ingrese la duración de la película ")

    #SQL que servirá para insertar los datos.
    sql = "INSERT INTO videos VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    #Insertando los datos.
    #El formato de la fecha tiene que ser mes/día/año.
    cursor1.execute(sql,(nombre, actores, genero, director, premio, fecha, link, duracion,))

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Modificar contenido. 
def modificar_contenido():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Las opciones para modificar contenido son las siguientes: \n")
    print("1. Modificar nombre")
    print("2. Modificar actores")
    print("3. Modificar género")
    print("4. Modificar director")
    print("5. Modificar premio")
    print("6. Modificar fecha")
    print("7. Modificar link")
    print("8. Modificar duración")
    print("9. Salir \n")

    decision = int(input("¿Cuál opción elige? "))

    if decision == 1: #Modificar el nombre de la película.
       
        print("Para modificar el nombre de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese el nuevo nombre: ")

                sql1 = "UPDATE videos SET nombre = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;
        
    elif decision == 2: #Actualizar nombres de actores.

        print("Para modificar el nombre de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese los nuevos nombres de los actores: ")

                sql1 = "UPDATE videos SET actor = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;
    
    elif decision == 3: #Modificar género.

        print("Para modificar el nombre de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese el género: ")

                sql1 = "UPDATE videos SET genero = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;
    
    elif decision == 4: #Modificar director.
        
        print("Para modificar el director de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese el nuevo nombre del director: ")

                sql1 = "UPDATE videos SET director = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;

    elif decision == 5: #Modificar premio.
        
        print("Para modificar el nombre de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese el nuevo nombre del promedio: ")

                sql1 = "UPDATE videos SET premio = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;
    elif decision == 6: #Modificar fecha.
        
        print("Para modificar el nombre de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese la nueva fecha de estreno (esta se debe colocar de la siguiente manera: mes/día/año): ")

                sql1 = "UPDATE videos SET fecha_streno = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;
    elif decision == 7: #Modificar link.
        
        print("Para modificar el link de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese el link del video: ")

                sql1 = "UPDATE videos SET link = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;
    elif decision == 8: #Modificar duración. 
        
        print("Para modificar la duración de la película, favor ingresar su nombre correctamente")
        
        #Pidiendo el nombre de la película.
        nombre = input("Ingrese el nombre de la película ")

        #Query a usar para buscar con el nombre.
        sql = "SELECT nombre FROM videos WHERE nombre = %s"

        #Ejecutando el query de búsqueda.
        cursor1.execute(sql, (nombre,))

        rows=cursor1.fetchall()

        #Imprimiendo el nombre de la película.
        for row in rows: 

            print(row[0])
            
            if nombre == row[0]:
                
                act = input("Ingrese la nueva duración: ")

                sql1 = "UPDATE videos SET duracion = %s WHERE nombre = %s"

                #Ejecutando el query de búsqueda.
                cursor1.execute(sql1, (act, nombre,))
                
                #Commit del query.
                conexion1.commit()

                #Cerrando la conexión.
                conexion1.close()
                
                print("Película actualizada \n")

                break;

    elif decision == 8: #Se eligió la opción para salir.
        print("Saliendo.....")
        modificar_contenido() #Regresando a la pantalla principal.

#Opción para eliminar el contenido.
def eliminar_contenido():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    nombre_película = input("Ingrese el nombre de la película que desea eliminar ")
    
    #Query a usar para buscar con el nombre.
    sql = "SELECT nombre FROM videos WHERE nombre = %s"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (nombre_película,))

    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 

        print(row[0])
        
        if nombre_película == row[0]:
            
            sql1 = "DELETE FROM videos WHERE nombre = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql1, (nombre_película,))
            
            #Commit del query.
            conexion1.commit()

            #Cerrando la conexión.
            conexion1.close()
            
            print("Película eliminada \n")

            break;