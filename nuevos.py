"""
Referencias: 

1. Generar nombres aleatorios:
    https://foroayuda.es/generar-nombres-aleatorios-ejemplo-de-codigo-de-python/

    Instalación: pip install namegenerator

2. Generar contraseñas aleatorias:
    https://geekflare.com/password-generator-python-code/

3. Listado de correos falsos: 
    https://sites.google.com/site/gruposcoutsanbruno1/principal/noticias/lista-actualizada-mails
"""

import namegenerator

import string
import random

from datetime import datetime #Librería para obtener la hora.

from datos import * #Importando los datos de la BD.
import psycopg2     #Importando la librería de la BD.

#Librería para encriptar las contraseñas.
import cryptocode

#Generar nombres aleatorios.
generador = int(input("Ingrese la cantidad de nombres que desea generar: "))

correos = ['c.analuz@yahoo.es', 'claudiocastanonmigeot@gmail.com', 'tango_negro@hotmail.com', 'pato_one@hotmail.com', '	javier_celedon@hotmail.com', 'fran.afull@live.cl', 'joacocordero@gmail.com', 'pepacordero@gmail.com'
               ,'laah.valehh@hotmail.com', 'annabeck_@hotmail.com', 'japacortes@yahoo.com', 'juanocortes@hotmail.com', 'pili_diami_angol@hotmail.com', 'tallerlaquilla@gmail.com', 'anamariadelacarrera@gmail.com', 'paulinadelacarrera@gmail.com'
               , 'fgregoriog@vtr.net', 'anto_demarchi@hotmail.com', '	Karito_1404@hotmail.com', 'loredicat@hotmail.com', 'diazma@tiscali.it', 'pablodubof@gmail.com', 'dddura69@gmail.com', 'khiton_@hotmail.com'
               , 'pecmor63@gmail.com', 'jlescote@gasco.cl', 'aespinz@hotmail.com', 'fespinosacl@yahoo.com', 'ricardo.espinosa.z@hotmail.com', 'sabelina50@yahoo.com.es', 'alvaro.espoz@gmail.com', 'patorfebre@hotmail.com', 'cfernandez@isa.cl', 
               'francis_nexos@hotmail.com', 'marcelafigueroazamora@hotmail.com', 'marcelafigueroazamora@hotmail.com', '	mafigza@gmail.com', 'marissaleone@hotmail.com', 'natygris@hotmail.com', 'consuelo.fornes@gmail.com', 
               'jmfornes@yahoo.com', 'fornickinson@hotmail.com', 'lml@vtr.net', 'xfreitte@gmail.com', 'fernandofreitte.xia@gmail.com', 'hfreitte2618@gmail.com', 'jfreitte@vtr.net', 'cfalvear@hotmail.com', 
               'debora1611@hotmail.com', 'fernando.gaete@gmail.com', 'fgaete@colegioaltamira.cl', 'panchop71@hotmail.com']

#Lista de nombres.
nombress = []

#Lista de apellidos.
apellidoss = []

#Lista de usuarios
usuarioss = []

## picking random characters from the list
password = ['32131', '32132', '32133', '32134', '32135','32136','32137','32138', '32139', '32140', '32141',	'32142','32143','32144', '32145','32146', '32147', '32148', '32149', '32150','32151', '32152', '32131', 
            '32132'	'32133', '32134', '32135', '32136', '32137', '32138', '32139', '32140', '32141', '32142', '32143', '32144', '32145', '32146', '32147', '32148', '32149', '32150', '32151', '32152', '32131', 
            '32132','32133', '46591', '32135','46593', '46595', '46589']

#Lista de perfiles
perfiless = []

planess = []

#Método para poder generar nombres aleatorios.
def nombres():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
        host=host(), #Host de la base de datos.
        user= user(), #Usuario de la base de datos.
        password=passw(), #Contraseña de la base de datos.
        database=BD(), #Base de datos que se usará.
        port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.


    now = datetime.now()

    sql = "INSERT INTO datos_usuario(nombre, apellido, usuario, contraseña, correo, plan, tiempo) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    sql2 = "INSERT INTO perfiles(usuario, perfil) VALUES (%s, %s)"

    print("Nombres \n")
    for i in range(generador):
        
        nombre = namegenerator.gen()

        print(nombre)

        
        apellido = apellidos()

        usuario = usuarios()

        contrasen = contrasenas()

        perf = perfiles()

        plan = seleccionPlanes(planes)

        cursor1.execute(sql,(nombre, apellido, usuario, contrasen, correos[i], plan, now,))
        cursor1.execute(sql2, (usuario, perf,))
    
    conexion1.commit()

    conexion1.close()


#Método para poder generar nombres aleatorios.
def apellidos():

    print("Apellidos")
    for i in range(generador):

        apellidos = namegenerator.gen() 
        
    return apellidos

#Método para poder generar perfiles aleatorios.
def usuarios():
    print("Usuario")
    for i in range(generador):

        usuario = namegenerator.gen() 
        print(usuario)

    return usuario

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#Método para generar contraseñas aleatorias.
def contrasenas(): 

    for i in range(generador):
        
        ff = random.choice(password)

        #Encriptando contraseña
        passkey = 'UVG' #Llave para encriptar.

        conn = cryptocode.encrypt(ff, passkey) #Contraseña encriptada.
        
        #print(conn)

    return conn

#Método para poder generar perfiles aleatorios.
def perfiles():

    print("Perfiles \n")
    for i in range(generador):
        
        perfiles = namegenerator.gen()

        print(perfiles)

    return perfiles

#Planes.
planes = ["Básico", "Estándar", "Avanzado"]

#Seleccionar de manera aleatoria los planes que pueden elegir los usuarios.
def seleccionPlanes(planes):
    print("Horas \n")
    for i in range(generador):

        ele = random.choice(planes)
        print(ele)

        return ele

def correo():

    for i in range(generador):
        print(correos[i])

    return correo[i]

nombres()
apellidos()
usuarios()
contrasenas()
perfiles()
seleccionPlanes(planes)
