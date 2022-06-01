"""
Por parte del programa se tiene que solicitar la fecha y la cantidad de visualizaciones que se desean hacer.
Referencias:
1. Como obtener un registro aleatorio: https://como.help/programacion/postgresql/como-seleccionarordenar-aleatoriamente-elementos-en-postgresql#:~:text=Si%20queremos%20solo%20obtener%20un,la%20mayoría%20de%20los%20casos.
2. Generar números aleatorios: https://j2logo.com/python/generar-numeros-aleatorios-en-python/
3. Generador de horas aleatorias: https://stackoverflow.com/questions/26740227/create-random-time-stamp-list-in-python
4. Dar formato a fechas: https://www.ipswitch.com/es/blog/formato-de-fecha-en-python#:~:text=El%20método%20strptime%20()%20le,el%20mes%20y%20el%20año.&text=Ahora%20que%20Python%20sabe%20que,otra%20cadena%20con%20formato%20diferente.
"""
from datos import * #Importando los datos de la BD.
import psycopg2     #Importando la librería de la BD.
import random
import datetime
from HoraRandom import *
from conexion import *

def generador():

    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #Pedirle al usuario la fecha y la cantidad de visualizaciones que se desean generar.
    año = int(input("Ingrese el año en la que desea hacer la simulación "))
    mes = int(input("Ingrese el mes en el que desea hacer la simulación "))
    dia = int(input("Ingrese el día en el que desea hacer la simulación "))
    cantidad = int(input("ingrese la cantidad de visualizaciones que desea generar en el sistema "))


    #Print de verificación.
    #print(startDate)
    print(cantidad)

    sql = "INSERT INTO historial VALUES(%s, %s, %s, %s, %s, %s)"

    #Haciendo loop de prueba. Este loop se corre en base a la cantidad de 
    #vistas que se quieren generar.
    for i in range(cantidad): 
        #print(fecha)

            #Horas aleatorias.
        hora = random.randint(0,23)
        mins = random.randint(0, 59)
        startDate = datetime.datetime(año, mes, dia, hora, mins)

        #Selección random de una película.
        sql1 = "SELECT RANDOM() AS orden, id, nombre, link FROM videos ORDER BY orden limit 1"
        
        cursor1.execute(sql1) #Corriendo el sql.

        a = cursor1.fetchall() #Guardando los datos obtenidos.

        print(a) #Trayendo la tupla de las películas. Esto es una lista de dos dimensiones.

        listaP = [a[0][1], a[0][2], a[0][3]] #Lista de las películas aleatorias a ver.

        print("Película obtenida", listaP[0], listaP[1], listaP[2]) #Aquí se está imprimiendo la película aleatoria con su id, nombre y link.

        #print(a[0][1])

        id = listaP[0] #Obteniendo el id de la película.
        nombre = listaP[1] #Obteniendo el nombre de la película.
        link = listaP[2] #Obteniendo el link de la película.

        #Seleccionando perfil aleatorio de prueba.
        sql2 = "SELECT RANDOM() AS orden, perfil FROM perfiles ORDER BY orden limit 1"

        cursor1.execute(sql2) #Corriendo el sql.
        
        b = cursor1.fetchall()

        print(b) #Imprimiendo la tupla que trae al usuario. Es un listado de dos dimensiones. 

        listaU = [b[0][1]] #Se guarda en la listaU solamente el nombre del perfil que se quiere meter a la BD.
        
        print("Perfil ", listaU[0]) #Imprimiendo al perfil que verá aleatoriamente la película.

        perfil = listaU[0] #Obteniendo el perfil que verá las películas.

        visto = 1 #Variable para el visto.

        """
        #Dando formato a las fechas y a las horas
        for x in random_date(startDate, cantidad):
            fecha1 = x.strftime("%Y-%m-%d %H:%M:%S")
        """
        cursor1.execute(sql, (perfil, nombre, link, visto, startDate, id,))

    conexion1.commit()

#generador()