import psycopg2 #Librería para la base de datos.
from datos import * #Trayendo la información de la Base Datos.

def traer_perfiles(usuario):
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    print("Los usuarios disponibles son: ")

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #SQL para poder jalar los perfiles de la base de datos.
    sql = "SELECT perfil FROM perfiles WHERE usuario = %s"

    #Trayendo los perfiles.
    cursor1.execute(sql, (usuario,)) #Ejecutando el query.
    rows=cursor1.fetchall()
    for row in rows:
        print(row[0]) #Imprimiendo los perfiles.
        perf = input("Ingrese el perfil que desee usar ")
        if perf == row[0]:
            print("¡Bienvendio " + row[0] + "!")
        else: #Si la persona elige mal el perfil, entoces se le dice que no está bien.
            print("Usuario mal redactado.")
            traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.

#Este es el menú que tendrá el usuario una vez pueda acceder a su perfil.
def menu_comercial():
    while True: 
        print("Hola")

usuario = "Javs"
traer_perfiles(usuario)