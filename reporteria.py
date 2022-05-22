"""
Nombres: Hansel López
         Javier Valle

Carnets: 19026
         20159
"""
from datos import * #Importando toda la info de la BD.
import psycopg2 #Importando librería para hacer la conexión con la BD.

def reporteria(): 
    print("Bienvenido a la pantalla de reportería \n")
    print("Las opciones de este módulo son las siguientes: ")
    print("1. Top 10 de géneros más vistos y los minutos consumidos para un rango de fechas dado")
    print("2. Cantidad de reproducciones por cada categoría, por tipo de cuenta para un rango de fechas dado")
    print("3. Top 10 de los directores y actores principales de las películas que los perfiles estándar y avanzados han visto")
    print("4. La cantidad de cuentas avanzadas que se han creado en los últimos 6 meses")
    print("5. Ver la hora pico donde el servicio es más usado para una fecha dada.")
    #Nuevo.
    print("6. Top 10 términos más buscados.")
    print("7. Ver el contenido más visto entre las 9:00 a.m. y la 1:00 a.m. para un mes dado")
    print("8. Top 20 películas que comenzaron a verse pero que llevan más de 20 días sin verse")
    print("9. Top 5 administradores que más modificaciones han realizado en las cuentas de usuarios para un rango de fechas dado")


    
    eleccion = int(input("¿Qué opción desea elegir? "))

    if eleccion == 1: #Ver el top 10 de géneros más vistos y los minutos consumidos para un rango de fechas dado.
        
        generos_mas_vistos_y_minutos_consumidos() #Método para ver los géneros más vistos y los minutos consumidos.

    elif eleccion == 2: #Cantidad de reproducciones por cada categoría, por tipo de cuenta para un rango de fechas dado.
        
        cant_reproducciones_por_tipo_cuenta_por_fechas() #Método que ve la cantida de reproducciones por tipo de cuenta en un rago de fechas dado.

    elif eleccion == 3: #Top 10 de los directores y actores principales de las películas que los perfiles estándar y avanzados han visto.
        
        top_10_directores_y_actores_por_perfiles_estandar_avanzados() #Método que ve el top 10 de los directores y actores principales de las películas que han visto los perfiles estándar y avanzado.
        
    elif eleccion == 4: #La cantidad de cuentas avanzadas que se han creado en los últimos seis meses.
        
        cant_cuentas_avanzadas() #Mëtodo que cuenta la cantidad de cuentas avanzadas que se crearon en los últimos seis meses.

    elif eleccion == 5: #Ver la hora pico donde el servicio es más usado para una fecha dada.
        
        hora_pico() #Método que determina la hora pico de una cierta fecha.

    elif eleccion == 6: #Ver el top 10 términos más buscados en la plataforma. (Nuevo)

        top_terminos_buscados() #Llamando al método para los términos más buscados en la plataforma.
    
    elif eleccion == 7:

        top5_contenido_mas_visto_en_un_mes() #Llamando al método que recoge los datos de las vistas para un mes dado. (Nuevo)
    
    elif eleccion == 8:

        top20_peliculas_sin_finalizar() #Método que ve cual es el top 20 películas que llevan más de 20 días sin terminarse. (Nuevo)
    
    elif eleccion == 9: #Método que ve cuales son los administradores que tienen más modificaciones en los usuarios. (Nuevo)
        top_adminis_modificaciones()


#Método para ver los géneros más vistos y los minutos consumidos.
def generos_mas_vistos_y_minutos_consumidos():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    print("Para ingresar las fechas que desea buscar, escríbalas de la siguiente forma: año-mes-día")

    fecha1 = input("Ingrese la fecha inicial: ")

    fecha2 = input("Ingrese la fecha final (la fecha final debe tener un día de atraso para ver mejor los datos): ")

    sql = "SELECT DISTINCT v.genero, TO_DATE(substring(tiempo, 0,11), 'YYYY/MM/DD') as fecha, sum(v.duracion) as minutos_consumidos FROM busquedas b JOIN videos v on b.busqueda = v.nombre WHERE tiempo >= %s and tiempo <= %s group by v.genero, b.tiempo limit 10"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (fecha1, fecha2,))
    
    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 
        print("Género|Fecha|Minutos Reproducidos")
        print(row) #Imprimiendo los datos de la BD.
    
    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método que sirve para ver la cantidad de reproducciones por tipo de cuenta en un rango de fechas.
def cant_reproducciones_por_tipo_cuenta_por_fechas():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    print("Para ingresar las fechas que desea buscar, escríbalas de la siguiente forma: año-mes-día")

    fecha1 = input("Ingrese la fecha inicial: ")

    fecha2 = input("Ingrese la fecha final (la fecha final debe tener un día de atraso para ver mejor los datos): ")

    #sql = "select distinct v.genero, TO_DATE(substring(b.tiempo, 0,11), 'YYYY/MM/DD') as fecha, count(b.busqueda) as minutos_consumidos, du.plan from busquedas b join videos v on b.busqueda = v.nombre join perfiles p on p.perfil = b.perfil join datos_usuario du on p.usuario = du.usuario where b.tiempo >= %s and b.tiempo <= %s group by v.genero, b.tiempo, du.plan, p.perfil"

    sql = "select v.genero, count(b.busqueda) as cantidad_reprodicciones from busquedas b join videos v on b.busqueda = v.nombre join perfiles p on p.perfil = b.perfil join datos_usuario du on p.usuario = du.usuario where b.tiempo >= %s and b.tiempo <= %s group by v.genero"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (fecha1, fecha2,))
    
    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 
        print("Género|Fecha Reproducción|Tipo de plan")
        print(row) #Imprimiendo los datos de la BD.
    
    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método que calcula el top 10 de directores y actores vistos por los perfiles estándar y avanzaods.
def top_10_directores_y_actores_por_perfiles_estandar_avanzados():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    print("Para ingresar las fechas que desea buscar, escríbalas de la siguiente forma: año-mes-día")

    fecha1 = input("Ingrese la fecha inicial: ")

    fecha2 = input("Ingrese la fecha final (la fecha final debe tener un día de atraso para ver mejor los datos): ")

    sql = "select v.director, v.actor, h.nombre, TO_DATE(substring(h.tiempo, 0,11), 'YYYY/MM/DD') as fecha from historial h join videos v on h.nombre = v.nombre join perfiles p on p.perfil = h.perfil join datos_usuario du on p.usuario = du.usuario where h.tiempo >= %s and h.tiempo <= %s and du.plan = 'Estándar' or du.plan = 'Avanzado' limit 10"

    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (fecha1, fecha2,))
    
    rows=cursor1.fetchall()
    #print(rows)

    #Imprimiendo el nombre de la película.
    for row in rows: 
        print("Director|Actores|Nombre|Fecha Estreno")
        print(row) #Imprimiendo los datos de la BD.
    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método que cuenta la cantidad de cuentas avanzadas creadas en los últimos seis meses.
def cant_cuentas_avanzadas():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    print("Para ingresar las fechas que desea buscar, escríbalas de la siguiente forma: año-mes-día")

    fecha1 = input("Ingrese la fecha inicial: ")

    fecha2 = input("Ingrese la fecha final (la fecha final debe tener un día de atraso para ver mejor los datos): ")

    sql = "select count(usuario), TO_DATE(substring(du.tiempo, 0,11), 'YYYY/MM/DD') as fecha from datos_usuario du where plan = 'Avanzado' and du.tiempo >= %s and du.tiempo <= %s group by du.tiempo"
    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (fecha1, fecha2,))
    
    rows=cursor1.fetchall()

    #Imprimiendo el nombre de la película.
    for row in rows: 
        print("Cuentas|Fecha Creación")
        print(row) #Imprimiendo los datos de la BD.
    
    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método que va a servir para determinar la hora pico del sistema.
def hora_pico():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    print("Para ingresar las fechas que desea buscar, escríbalas de la siguiente forma: año-mes-día")

    fecha1 = input("Ingrese la fecha inicial: ")

    #fecha2 = input("Ingrese la fecha final (la fecha final debe tener un día de atraso para ver mejor los datos): ")

    sql = "select TO_DATE(substring(b.tiempo, 0,11), 'YYYY/MM/DD') as fecha, b.tiempo from busquedas b where b.tiempo > %s order by TO_DATE(substring(b.tiempo, 0,11), 'YYYY/MM/DD') desc"
    
    #Ejecutando el query de búsqueda.
    cursor1.execute(sql, (fecha1,))
    
    rows=cursor1.fetchall()
    
    #print(rows)

    #Imprimiendo las horas de búsqueda de manera descendiente.
    for row in rows:
        print(row)
    
    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Función para poder ver el top de términos más buscados en la plataforma de streaming.
def top_terminos_buscados():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    print("A continuación se le presentarán los términos más buscados en la plataforma.")

    cursor1.execute("select * from buscar")

    rows = cursor1.fetchall()

    for row in rows:
        print(row[0])

    #Commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método para poder ver el contenido más visto en cada hora entre 9:00 a.m. a 1:00 a.m. para un mes dado. 
def top5_contenido_mas_visto_en_un_mes():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    #Se está pidiendo el mes en el que se desea ver el contenido más visto entre las 9:00 a.m. y la 1:00 a.m.
    mes = int(input("Ingrese el mes que desea ver el contenido más visto entre las 9:00 a.m. y la 1:00 a.m. "))

    #Preparando el query para la selección.
    sql = "SELECT * FROM get_top(%s)"

    #Ejectuando el query.
    cursor1.execute(sql, (mes,))

    #Haciendo fetch de los datos a jalar.
    rows = cursor1.fetchall()

    #Imprimiendo todo lo que se jaló.
    print("Mes       Hora        Título")
    for row in rows:
        print(row[0], row[1], row[2])

    #Haciendo commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método que jala el top 20 de películas que comenzaron a verse pero que llevan más de 20 días son finalizarse, para un rango de fechas dado.
def top20_peliculas_sin_finalizar():
    
    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    fecha1 = input("Ingrese la fecha inicial (esta debe ir de esta forma MM-DD-YYYY) ") #Ingresando la fecha inicial del reporte.
    fecha2 = input("Ingrese la fecha final (esta debe ir de esta forma MM-DD-YYYY) esta tiene que ir con un día de atraso ") #Ingresando la fecha inicial del reporte.

    sql = "SELECT * FROM get_rangos(%s, %s)"

    cursor1.execute(sql, (fecha1,fecha2,))

    rows = cursor1.fetchall()

    for row in rows:
        print(row[0], row[1])

    #Haciendo commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

#Método que jala el top de administradores que más modificaciones para un rango de fechas dado.
def top_adminis_modificaciones():
        #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.

    fecha1 = input("Ingrese la fecha inicial (esta debe ir de esta forma MM-DD-YYYY) ") #Ingresando la fecha inicial del reporte.
    fecha2 = input("Ingrese la fecha final (esta debe ir de esta forma MM-DD-YYYY) esta tiene que ir con un día de atraso ") #Ingresando la fecha inicial del reporte.

    sql = "SELECT * FROM get_mods(%s, %s)" #SQL que invoca a la función que trae al top de administradores con más modificaciones.

    cursor1.execute(sql, (fecha1,fecha2,))

    rows = cursor1.fetchall()

    for row in rows:
        print(row[0], row[1])

    #Haciendo commit del query.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()
