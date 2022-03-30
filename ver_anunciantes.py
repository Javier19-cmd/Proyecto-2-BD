from datos import * #Importando todos los datos de la base de datos.
import psycopg2 #Librería para abrir la base de datos.

#Método principal del archivo.
def ver_anunciantes():
    while True: 
        print("Bienvenido a la página para ver a los anunciantes y sus datos \n")
        print("Las opciones son las siguientes: \n")
        print("1. Agregar anunciantes")
        print("2. Modificar datos de anunciantes")
        print("3. Eliminar anunciantes")
        print("4. Agregar contenido")
        print("5. Modificar contenido")
        print("6. Quitar contenido")

        try: 
            eleccion = int(input("¿Qué opción elije? "))
            
            if eleccion == 1: #Agregar anunciantes.
                
                agregar_anunciante() #Método que agrega anunciantes.

            elif eleccion == 2: #Modificar datos de anunciantes.
                print("Hola")
            elif eleccion == 3: #Eliminar anunciantes.
                print("Hola")
            elif eleccion == 4: #Agregar contenido.
                print("Hola")
            elif eleccion == 5: #Modificar contenido.
                print("Hola")
            elif eleccion == 6: #Salir de la pantalla.
                print("Saliendo......")
                break;

        except:
            print("Opción no válida")


#Método para agregar anunciante.
def agregar_anunciante():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(
            host=host(), #Host de la base de datos.
            user= user(), #Usuario de la base de datos.
            password=passw(), #Contraseña de la base de datos.
            database=BD(), #Base de datos que se usará.
            port=port() #Puerto de la base de datos.
    )

    cursor1 = conexion1.cursor() #Cursor de la conexión.
    
    nombre = input("Ingrese el nombre del anunciante ")#Pidiendo nombre del anunciante.

    correo = input("Ingrese el correo del anunciante ")#Pidiendo el correo del anunciante.

    #SQL para insertar los datos en una tabla.
    sql = "INSERT INTO anunciante VALUES (%s, %s)"

    #Corriendo el sql.
    cursor1.execute(sql, (nombre, correo,))

        #Haciendo commit de los queries.
    conexion1.commit()

    #Cerrando la conexión.
    conexion1.close()

    print("Anunciante agregado")

ver_anunciantes()