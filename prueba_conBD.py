"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
import psycopg2 #Librería para la base de datos.
from datos import *

def probando():
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host='project2db-do-user-11101874-0.b.db.ondigitalocean.com',
            user= user(),
            password='aYSwBxxQYMU9ZQmJ',
            database='dbproject2',
            port='25060'
    )

    #Creando cursor. Recorre la base de datos.
    cursor1=conexion1.cursor()

    #Query a usar.
    sql = "insert into test(test) values (%s)"

    #Input del usuario.
    a = input("Ingrese dato: \n") 

    #Ejecutando el query del insert. Siempre se tiene que poner una coma después de la última variable a insertar.
    cursor1.execute(sql,(a,))

    #Forma de hacer el select.
    cursor1.execute("SELECT * FROM test")
    rows=cursor1.fetchall()
    for row in rows: 
        print(row)

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

probando()