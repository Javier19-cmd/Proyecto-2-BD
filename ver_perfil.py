#Importando todos los datos del perfil.
from datos import *

#Método para ver el perfil.
def ver():
    while True:
        print("Bienvenido al menú para ver el perfil, ¿qué desea hacer? \n")
        print("1) Hacer downgrade")
        try: 
            eleccion = int(input("Elija su opción \n"))
            
            if eleccion == 1: #Hacer downgrade
                
                print("Opción de downgrade elegida \n")
                downgrade() #Opción de downgrade elegida.

            else: #Opción mayor o menor a uno
                
                print("Opción no válida")

        except: 
            print("Opción no numérica")

#Opción para hacer el downgrade
def downgrade():
    print("Hacer downgrade")



ver()#Probando.