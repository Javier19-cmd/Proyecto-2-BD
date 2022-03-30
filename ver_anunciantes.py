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
            eleccion = int(input("¿Qué opción elije?"))
            
            if eleccion == 1: #Agregar anunciantes.
                print("Hola")
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
    print("Hola")
ver_anunciantes()