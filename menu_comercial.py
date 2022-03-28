import psycopg2 #Librería para la base de datos.
from datos import * #Trayendo la información de la Base Datos.
from ver_perfil import * #Trayendo las opciones para ver el perfil.

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

    for row1 in rows1: 
        if row1[0] == 'Básico':
            cursor1.execute(sql2,(usuario,))
            rows2 = cursor1.fetchall()
            for row in rows2:
                print(row[0]) #Imprimiendo los perfiles.
                perf = input("Ingrese el perfil que desee usar ")
                if perf == row[0]:
                    print("¡Bienvendio " + row[0] + "!")
                    menu_comercial() #Trayendo el menú comercial a la pantalla del usuario.
                else: #Si la persona elige mal el perfil, entoces se le dice que no está bien.
                    print("Usuario mal redactado.")
                    traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.
        
        elif row1[0] == 'Estándar':
            cursor1.execute(sql3,(usuario,))
            rows2 = cursor1.fetchall()
            for row1 in rows2:
                print(row1[0]) #Imprimiendo los perfiles.
                perf = input("Ingrese el perfil que desee usar ")
                if perf == row1[0]:
                    print("¡Bienvendio " + row1[0] + "!")
                    menu_comercial() #Trayendo el menú comercial a la pantalla del usuario.
                else: #Si la persona elige mal el perfil, entoces se le dice que no está bien.
                    print("Usuario mal redactado.")
                    traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.
        
        elif row[0] == 'Avanzado':
            cursor1.execute(sql4,(usuario,))
            rows2 = cursor1.fetchall()
            for row2 in rows2:
                print(row2[0]) #Imprimiendo los perfiles.
                perf = input("Ingrese el perfil que desee usar ")
                if perf == row2[0]:
                    print("¡Bienvendio " + row2[0] + "!")
                    menu_comercial() #Trayendo el menú comercial a la pantalla del usuario.
                else: #Si la persona elige mal el perfil, entoces se le dice que no está bien.
                    print("Usuario mal redactado.")
                    traer_perfiles(usuario) #Se pone a elegir otra vez para que redacte bien el perfil.

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
def menu_comercial():
    while True: 
        print("Las opciones que hay son: \n")
        print("1. Ver perfil")
        print("2. Buscar películas")
        print("3. Ver lista de favoritos")
        print("4. Salir \n")

        #Try-catch para evitar clavos.
        try: 
            eleccion = int(input("¿Cuál opción elige? ")) #Variable numérica.

            if eleccion == 1: 
                #Opción para ver el perfil.
                ver() #Opción para hacer downgrade.
            elif eleccion == 2: 
                #Opción para buscar película.
                print("Hola")
            elif eleccion == 3:
                #Opción para ver lista de favoritos. 
                print("Hola")
            elif eleccion == 4: 
                #Salir de la pantalla.
                print("Saliendo....")
                break;
            else: #Se eligió una opción mayor o menor a 4.
                print("Opción no válida")
        except:
            #Se puso una opción que no era número.
            print("Se eligió una opción no numérica")