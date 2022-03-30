from datos import * #Importando todos los datos de la base de datos.
import psycopg2 #Librería para abrir la base de datos.

#Método principal del archivo.
def ver_anunciantes():
    while True: 
        print("Bienvenido a la página para ver a los anunciantes y sus datos \n")
        print("Las opciones son las siguientes \n")
        print("")

ver_anunciantes()