"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
from datos import * #Importando todos los datos de la base de datos.
import psycopg2 #Librería para abrir la base de datos.
from conexion import *

#Método principal del archivo.
def ver_anunciantes():
    while True: 
        print("Bienvenido a la página para ver a los anunciantes y sus datos \n")
        print("Las opciones son las siguientes: \n")
        print("1. Agregar anunciantes")
        print("2. Modificar datos de anunciantes")
        print("3. Eliminar anunciantes")
        print("4. Agregar contenido")
        print("5. Modificar contenido")
        print("6. Quitar contenido")
        print("7. Salir")

        try: 
            eleccion = int(input("¿Qué opción elije? "))
            
            if eleccion == 1: #Agregar anunciantes.
                
                agregar_anunciante() #Método que agrega anunciantes.

            elif eleccion == 2: #Modificar datos de anunciantes.
                
                modificar_anunciante() #Método para modificar a un anunciante.

            elif eleccion == 3: #Eliminar anunciantes.

                eliminar_anunciante() #Método para eliminar anunciante.
            
            elif eleccion == 4: #Agregar contenido.
                
                agregar_contenido() #Método para agregar contenido.

            elif eleccion == 5: #Modificar contenido.

                modificar_contenidoo() #Método para modificar contenido.
            
            elif eleccion == 6: #Quitar contenido.

                quitar_auncio() #Método para quitar anuncio.
            
            elif eleccion == 7: #Salir de la pantalla. 
                print("Saliendo....")
                break;

        except:
            print("Opción no válida")


#Método para agregar anunciante.
def agregar_anunciante():

    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    nombre = input("Ingrese el nombre del anunciante ")#Pidiendo nombre del anunciante.

    correo = input("Ingrese el correo del anunciante ")#Pidiendo el correo del anunciante.

    #SQL para insertar los datos en una tabla.
    sql = "INSERT INTO anunciante VALUES (%s, %s)"

    #Corriendo el sql.
    cursor1.execute(sql, (nombre, correo,))

        #Haciendo commit de los queries.
    conexion1.commit()

    print("Anunciante agregado")

#Método para modificar anunciantes.
def modificar_anunciante():
    
    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Para el correo del anunciante, ingrese el nombre del anunciante ")
        
    #Pidiendo el usuario del anunciante.
    nombre = input("Ingrese nombre del anunciante ")

    #Query a usar para buscar con el nombre.
    sql = "SELECT nombre FROM anunciante WHERE nombre = %s"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (nombre,))

    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 

        print(row[0])
        
        if nombre == row[0]:
            
            act = input("Ingrese el nuevo correo del anunciante: ")

            sql1 = "UPDATE anunciante SET correo = %s WHERE nombre = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql1, (act, nombre,))
            
            #Commit del query.
            conexion1.commit()
            
            print("Correo actualizado \n")

            break;

def eliminar_anunciante():

    #Conexión a la base de datos.
    conexion1 = getConnection()
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    nombre = input("Por favor escriba el anunciante que desea dar debaja ")

    #SQL para eliminar datos de la persona.
    sql = "DELETE FROM anunciante WHERE nombre = %s"

    #SQL para eliminar perfiles de la persona.
    sql2 = "DELETE FROM anuncio WHERE nombre_anunciante = %s"

    #Ejecutando los queries de eliminación. Primero se eliminó el anuncio del anunciante y luego al anunciante.
    cursor1.execute(sql2, (nombre,)) #Eliminando anunciante de la tabla anunciante.

    cursor1.execute(sql, (nombre,)) #Eliminando los anuncios del anunciante.

    #Haciendo commit de los queries.
    conexion1.commit()

    print("Anunciante eliminado")

#Método para agregar contenido.
def agregar_contenido():
    
    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    nombre = input("Ingrese el nombre del anunciante ")#Pidiendo nombre del anunciante.

    link = input("Ingrese el link del anuncio ")#Pidiendo el link del anuncio.

    genero = input("Ingrese el género del anuncio ") #Pidiendo el género del anuncio.

    #SQL para insertar los datos en una tabla.
    sql = "INSERT INTO anuncio VALUES (%s, %s, %s)"

    #Corriendo el sql.
    cursor1.execute(sql, (nombre, link, genero,))

        #Haciendo commit de los queries.
    conexion1.commit()

    print("Anunciante agregado")

#Método para modificar contenido.
def modificar_contenidoo():

    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("Para modificar contenido están las siguientes opciones\n")
    print("1. Modificar link")
    print("2. Modificar género")

    try: 
        dec = int(input("Ingrese su decisión: "))

        if dec == 1: #Modificar link del anuncio.
            
            #Pidiendo el nombre del anunciante.
            nombre = input("Ingrese nombre del anunciante ")

            #Query a usar para buscar con el nombre.
            sql = "SELECT nombre_anunciante FROM anuncio WHERE nombre_anunciante = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql, (nombre,))

            rows=cursor1.fetchall()

            #Imprimiendo el nombre de la película.
            for row in rows: 

                print(row[0])
                
                if nombre == row[0]:
                    
                    act = input("Ingrese el link del anuncio: ")

                    sql1 = "UPDATE anuncio SET link = %s WHERE nombre_anunciante = %s"

                    #Ejecutando el query de búsqueda.
                    cursor1.execute(sql1, (act, nombre,))
                    
                    #Commit del query.
                    conexion1.commit()
                    
                    print("Link actualizado \n")

                    break;

        elif dec == 2: #Modificar género.
            
            #Pidiendo el nombre del anunciante.
            nombre = input("Ingrese nombre del anunciante ")

            #Query a usar para buscar con el nombre.
            sql = "SELECT nombre_anunciante FROM anuncio WHERE nombre_anunciante = %s"

            #Ejecutando el query de búsqueda.
            cursor1.execute(sql, (nombre,))

            rows=cursor1.fetchall()

            #Imprimiendo el nombre de la película.
            for row in rows: 

                print(row[0])
                
                if nombre == row[0]:
                    
                    act = input("Ingrese el género del anuncio: ")

                    sql1 = "UPDATE anuncio SET genero = %s WHERE nombre_anunciante = %s"

                    #Ejecutando el query de búsqueda.
                    cursor1.execute(sql1, (act, nombre,))
                    
                    #Commit del query.
                    conexion1.commit()
                    
                    print("Género actualizado \n")

                    break;
        else: 
            print("Opción no válida")
    
    except: 
        print("Opción no numérica")

#Método para quitar anuncios.
def quitar_auncio():
    
    #Conexión a la base de datos.
    conexion1 = getConnection()
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    nombre = input("Por favor escriba el anuncio que desea quitar ")

    #SQL para eliminar perfiles de la persona.
    sql2 = "DELETE FROM anuncio WHERE nombre_anunciante = %s"

    #Ejecutando los queries de eliminación. Primero se eliminó el anuncio del anunciante y luego al anunciante.
    cursor1.execute(sql2, (nombre,)) #Eliminando anunciante de la tabla anunciante.

    #Haciendo commit de los queries.
    conexion1.commit()

    print("Anuncio eliminado")