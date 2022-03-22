#Archivo que se encarga de registrar a las personas en la base de datos.
def registro():
    #Menú para registrar a las personas en la base de datos.
    print("Bienvenid@ a la página de registro de la plataforma de streaming \n")

    nombre = input("Ingrese su nombre: ")

    apellido = input("Ingrese su apellido: ")

    usuario = input("Ingrese su usuario: ")

    contraseña = input("Ingrese su contraseña: ")

    correo = input("Ingrese su correo: ")
    
    #Plan básico, estándar y avanzado.
    plan = input("Ingrese su plan: ")