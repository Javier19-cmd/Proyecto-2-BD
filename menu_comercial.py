"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""

import psycopg2 #Librería para la base de datos.
import datetime #Librería para poder usar fechas.
from datos import * #Trayendo la información de la Base Datos.
from ver_perfil import * #Trayendo las opciones para ver el perfil.
from buscar import * #Trayendo las opciones de buscar.
from favoritos import * #Trayendo las opciones para agregar contenido a su lista de favoritos.
from anuncios import * #Trayendo la clase para agregar anuncios.

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

    #Obteniendo el plan del usuario.
    plan = "SELECT plan FROM datos_usuario WHERE usuario = %s"

    #Perfil gratis
    sql2 = "SELECT p.perfil FROM datos_usuario du join perfiles p on du.usuario = p.usuario WHERE du.usuario = %s limit 1"

    #Perfil básico 
    sql3 = "SELECT p.perfil FROM datos_usuario du join perfiles p on du.usuario = p.usuario WHERE du.usuario = %s limit 4"

    #Perfil avanzado
    sql4 = "SELECT p.perfil FROM datos_usuario du join perfiles p on du.usuario = p.usuario WHERE du.usuario = %s limit 8"

    #Trayendo los planes de la base de datos.
    cursor1.execute(plan, (usuario,))
    rows1 = cursor1.fetchall()

    #print(rows1)

    for row1 in rows1: 
        if row1[0] == 'Básico':
            cursor1.execute(sql2,(usuario,))
            rows2 = cursor1.fetchall()

            a = [] #Lista para guardar los perfiles que se van a imprimir.

            #Guardando los perfiles que se trajeron.
            for cosa in rows2:
                a.append(cosa[0])
            
            print(a) #Imprimiendo los perfiles.

            perf = input("Ingrese el perfil que desee usar ") #Pidiendo el perfil que desea usar.

            #Viendo si el perfil ya ingresó o no. Se jala el ingreso del perfil.
            sql = "SELECT ingreso FROM perfiles WHERE perfil = %s"
            cursor1.execute(sql, (perf,))
            rowss = cursor1.fetchall()

            entrada = [] #Lista para ver si el perfil ya ingresó o no.
            
            #Guardando la propiedad de que entró o no.
            for ent in rowss:
                entrada.append(ent[0])
            
            #Variable para ver si el perfil ya ingresó o no.
            confir = 0
            
            #Recorriendo la lista y comprobando que el perfil sí exista.
            if perf in a:
                if confir in entrada:
                    print("¡Bienvendio " + perf + "!")
                    #Actuaizando el ingreso de la persona.
                    sql = "UPDATE perfiles SET ingreso = %s WHERE perfil = %s"
                    ing = 1
                    cursor1.execute(sql, (ing, perf,))
                    conexion1.commit()
                    menu_comercial(usuario, perf) #Trayendo el menú comercial a la pantalla del usuario.
                else:
                    print("Usuario activo.")
            else:
                print("Usuario mal redactado.")
                traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.
        
        elif row1[0] == 'Estándar':
            cursor1.execute(sql3,(usuario,))
            rows2 = cursor1.fetchall()

            a = [] #Lista para guardar los perfiles que se van a imprimir.

            #Guardando los perfiles que se trajeron.
            for cosa in rows2:
                a.append(cosa[0])
            
            print(a) #Imprimiendo los perfiles.

            perf = input("Ingrese el perfil que desee usar ") #Pidiendo el perfil que desea usar.

            #Viendo si el perfil ya ingresó o no. Se jala el ingreso del perfil.
            sql = "SELECT ingreso FROM perfiles WHERE perfil = %s"
            cursor1.execute(sql, (perf,))
            rowss = cursor1.fetchall()

            entrada = [] #Lista para ver si el perfil ya ingresó o no.
            
            #Guardando la propiedad de que entró o no.
            for ent in rowss:
                entrada.append(ent[0])
            
            #Variable para ver si el perfil ya ingresó o no.
            confir = 0
            
            #Recorriendo la lista y comprobando que el perfil sí exista.
            if perf in a:
                if confir in entrada:
                    print("¡Bienvendio " + perf + "!")
                    #Actuaizando el ingreso de la persona.
                    sql = "UPDATE perfiles SET ingreso = %s WHERE perfil = %s"
                    ing = 1
                    cursor1.execute(sql, (ing, perf,))
                    conexion1.commit()
                    menu_comercial(usuario, perf) #Trayendo el menú comercial a la pantalla del usuario.
                else:
                    print("Usuario activo.")
            else:
                print("Usuario mal redactado.")
                traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.
        
        elif row1[0] == 'Avanzado':
            cursor1.execute(sql4,(usuario,))
            rows2 = cursor1.fetchall()
            #print(rows2[0][0])

            a = [] #Lista para guardar los perfiles que se van a imprimir.

            #Guardando los perfiles que se trajeron.
            for cosa in rows2:
                a.append(cosa[0])
            
            print(a) #Imprimiendo los perfiles.

            perf = input("Ingrese el perfil que desee usar ") #Pidiendo el perfil que desea usar.

            #Viendo si el perfil ya ingresó o no. Se jala el ingreso del perfil.
            sql = "SELECT ingreso FROM perfiles WHERE perfil = %s"
            cursor1.execute(sql, (perf,))
            rowss = cursor1.fetchall()

            entrada = [] #Lista para ver si el perfil ya ingresó o no.
            
            #Guardando la propiedad de que entró o no.
            for ent in rowss:
                entrada.append(ent[0])
            
            #Variable para ver si el perfil ya ingresó o no.
            confir = 0
            
            #Recorriendo la lista y comprobando que el perfil sí exista.
            if perf in a:
                if confir in entrada:
                    print("¡Bienvendio " + perf + "!")
                    #Actuaizando el ingreso de la persona.
                    sql = "UPDATE perfiles SET ingreso = %s WHERE perfil = %s"
                    ing = 1
                    cursor1.execute(sql, (ing, perf,))
                    conexion1.commit()
                    menu_comercial(usuario, perf) #Trayendo el menú comercial a la pantalla del usuario.
                else:
                    print("Usuario activo.")
            else:
                print("Usuario mal redactado.")
                traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.

            """

            for row2 in rows2:
                #print(row2[0]) #Imprimiendo los perfiles.
                perf = input("Ingrese el perfil que desee usar ")
                if perf == row2[0]:
                    print("¡Bienvendio " + row2[0] + "!")
                    
                    menu_comercial(usuario, perf) #Trayendo el menú comercial a la pantalla del usuario.
                else: #Si la persona elige mal el perfil, entoces se le dice que no está bien.
                    print("Usuario mal redactado.")
                    traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.
                    """

    """
    #Trayendo los perfiles.
    cursor1.execute(sql, (usuario,)) #Ejecutando el query.
    rows=cursor1.fetchall()
    for row in rows:
        print(row[0]) #Imprimiendo los perfiles.
        perf = input("Ingrese el perfil que desee usar ")
        if perf == row[0]:
            print("¡Bienvendio " + row[0] + "!")
            menu_comercial() #Trayendo el menú comercial a la pantalla del usuario.
        else: #Si la persona elige mal el perfil, entoces se le dice que no está bien.
            print("Usuario mal redactado.")
            traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.
    """

#Este es el menú que tendrá el usuario una vez pueda acceder a su perfil.
def menu_comercial(usuario, perfil):
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    while True: 
        print("Las opciones que hay son: \n")
        print("1. Ver perfil")
        print("2. Buscar películas")
        print("3. Ver lista de favoritos")
        print("4. Salir \n")

        anuncios(usuario) #Módulo que enseña los anuncios. Viene de la clase de anuncios.

        #Try-catch para evitar clavos.
        try: 
            eleccion = int(input("¿Cuál opción elige? ")) #Variable numérica.

            if eleccion == 1: 
                #Opción para ver el perfil.
                ver(usuario) #Opción para hacer downgrade. #Opción de la clase de ver_perfil.
            elif eleccion == 2: 
                #Opción para buscar película.
                buscar(perfil) #Opción para buscar. Esta se trae de la clase buscar.
            elif eleccion == 3:
                #Opción para ver lista de favoritos. 
                favoritos(perfil) #Opción para buscar. Opción de la clase favoritos.
            elif eleccion == 4: 
                #Salir de la pantalla.
                print("Saliendo....")
                #Actualizar el ingreso del perfil.
                ingre = 0
                sql = "UPDATE perfiles SET ingreso = %s WHERE perfil = %s"
                cursor1.execute(sql, (ingre, perfil,))
                conexion1.commit()
                break;
            else: #Se eligió una opción mayor o menor a 4.
                print("Opción no válida")
        except:
            #Se puso una opción que no era número.
            print("Se eligió una opción no numérica")

