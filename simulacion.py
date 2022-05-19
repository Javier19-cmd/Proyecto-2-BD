"""
Por parte del programa se tiene que solicitar la fecha y la cantidad de visualizaciones que se desean hacer.
"""
from datos import * #Importando los datos de la BD.
import psycopg2     #Importando la librería de la BD.
import random 

def generador():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #Pedirle al usuario la fecha y la cantidad de visualizaciones que se desean generar.
    fecha = input("Ingrese la fecha en la que desea hacer la simulación (esta deber ir como MM-DD-YYYY) ")
    cantidad = int(input("ingrese la cantidad de visualizaciones que desea generar en el sistema "))

    #Print de verificación.
    print(fecha)
    print(cantidad)

    sql = "INSERT INTO prueba VALUES(%s)"

    sql1 = "SELECT id FROM videos"

    num = cursor1.execute(sql1)

    ruleta = random.randint(0, num)

    print(ruleta)
    
    #Haciendo loop de prueba.
    for i in range(cantidad): 
        print(fecha)

        cursor1.execute(sql, (fecha,))

    conexion1.commit()

    conexion1.close()

generador()