"""
Referencias: 

1. https://pythonbros.com/como-generar-numeros-random-con-python/

"""

from datos import * #Importando los datos de la BD.
import psycopg2 #Importando librería que conecta con postgres.
import random #Librería para generar números aleatorios.

#Archivo que se va a encargar de generar los anuncios de la plataforma.
def anuncios (usuario):

    """
    Géneros a usar: 

    1. Acción
    2. Romance
    3. Comedia
    4. Suspenso
    """

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )
    
    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #SQL para seleccionar usuario.
    sql = "SELECT plan FROM datos_usuario WHERE usuario = %s"

    #Verificando que el usuario sí exista en la tabla.
    cursor1.execute(sql, (usuario,))
    rows=cursor1.fetchall()
    
    #Validando que el usuario tenga el plan básico.
    for row in rows:
        if row[0] == "Básico": 
            
            print("Anuncio: \n")

            numero = random.randint(1,4) #Generando número aleatorio para que se impriman los anuncios.

            if numero == 1: #Imprimiendo anuncios de acción.

                genero = "Acción"
                
                #SQL para jalar el anuncio
                sql2 = "SELECT link FROM anuncio WHERE genero = %s"

                cursor1.execute(sql2, (genero,))
                rows2=cursor1.fetchall()

                #Imprimiendo anuncio.
                for row2 in rows2: 
                    print(row2[0])
                    print("\n")
            
            elif numero == 2: #Imprimiendo anuncios de romance.
                
                genero = "Romance"
                
                #SQL para jalar el anuncio
                sql2 = "SELECT link FROM anuncio WHERE genero = %s"

                cursor1.execute(sql2, (genero,))
                rows2=cursor1.fetchall()

                #Imprimiendo anuncio.
                for row2 in rows2: 
                    print(row2[0])
                    print("\n")
            
            elif numero == 3: #Imprimiendo anuncios de comedia.
                
                genero = "Comedia"
                
                #SQL para jalar el anuncio
                sql2 = "SELECT link FROM anuncio WHERE genero = %s"

                cursor1.execute(sql2, (genero,))
                rows2=cursor1.fetchall()

                #Imprimiendo anuncio.
                for row2 in rows2: 
                    print(row2[0])
                    print("\n")
            
            elif numero == 4: #Imprimiendo anuncios de suspenso.
                
                genero = "Suspenso"
                
                #SQL para jalar el anuncio
                sql2 = "SELECT link FROM anuncio WHERE genero = %s"

                cursor1.execute(sql2, (genero,))
                rows2=cursor1.fetchall()

                #Imprimiendo anuncio.
                for row2 in rows2: 
                    print(row2[0])
                    print("\n")

        else: 
            print(":v")