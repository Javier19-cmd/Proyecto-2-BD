"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
import psycopg2 #Librería para la base de datos.
from datos import * #Trayendo la información de la Base Datos.
from modificar_contenido import * #Trayendo la clase que servirá para modificar el contenido de las películas.
from ver_usuarios import * #Trayendo todo lo que servirá para modificar el contenido de la base de datos.
from ver_anunciantes import * #Trayendo todo lo que servirá para modificar a los anunciantes y a su contenido.
from reporteria import * #Importando todo lo que sirve para la reportería.
from registro_admins import * #Importando el registro de administradores.
from simulacion import * #Importando el método que se encarga de la simulación.
from conexion import *

#Este menú se va a enseñar una vez ya se haya iniciado sesión como administrador.
def menu_admin(usuario):
    
    #Conexión a la base de datos.
    conexion1 = getConnection()

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    while True: 
        print("1. Ver contenido")
        print("2. Ver usuarios")
        print("3. Ver contenido de anuncios")
        print("4. Módulo de reportería")
        print("5. Agregar nuevo usuario administrador") #Nuevo
        print("6. Simular día de operaciones") #Nuevo
        print("7. Salir \n")
        
        #Try-catch del menú.
        try: 
            decision = int(input("¿Cuál opción elige? "))
            if decision == 1:#Ver contenido.
                modificar_contenidos() #Perteneciente a la clase de modificar_contenido.
            elif decision == 2:#Ver usuarios.
                ver_usuarios() #Perteneciente a la clase de modificar_contenido.
            elif decision == 3:
                #Ver contenido de anuncios. 
                ver_anunciantes() #Perteneciente a la clase ver_anunciantes.
            elif decision == 4:
                reporteria() #Perteneciente a la clase de reportería.
            elif decision == 5: #Nuevo.
                registrar_admin() #Llamando al registro de administradores.
            elif decision == 6: #Nuevo.
                generador() #Llamando al simulador de las visualizaciones.
            elif decision == 7: #Saliendo de la pantalla. 
                #Salir al menú principal.
                print("Saliendo....")

                ingre = 0
                sql = "UPDATE admins SET ingreso = %s WHERE usuario = %s"
                cursor1.execute(sql, (ingre, usuario,))
                conexion1.commit()
                conexion = getConnection()
                print("cerrando conexion...")
                disconnect(conexion)
                break;
            else: #Opción no válida.
                print("Opción no válida.") 
        except: 
            #Opción no numérica elegida.
            print("Opción no numérica ingresada")