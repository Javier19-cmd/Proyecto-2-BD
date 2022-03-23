#Importando los datos de la BD.
from datos import *

#Opciones para registrar a los perfiles del sistema.

def basico():
    #El usuario solo puede tener como máximo a un usuario. 
    perfil = input("Ingrese el nombre del perfil: ")

def estandar():
    while True:
        #El usuario puede elegir como máximo a cuatro perfiles.
        decision = int(input("¿Cuántos perfiles desea tener? "))

        if decision == 1: 
            #El usuario eligió a dos perfiles.
            perfil = input("Ingrese el nombre del usuario: ")
        elif decision == 2: 
            #El usuario eligió a dos perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
        
        elif decision == 3: 
            #El usuario eligió a tres perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
        
        elif decision == 4: 
            #El usuario eligió a cuatro perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
        else: 
            #Se eligieron más perfiles.
            print("No se pueden elegir más perfiles.")


def avanzado():
    #El usuario puede elegir como máximo a ocho perfiles.
    while True:
        #El usuario puede elegir como máximo a cuatro perfiles.
        decision = int(input("¿Cuántos perfiles desea tener? "))

        if decision == 1: 
            #El usuario eligió a dos perfiles.
            perfil = input("Ingrese el nombre del usuario: ")
        elif decision == 2: 
            #El usuario eligió a dos perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
        
        elif decision == 3: 
            #El usuario eligió a tres perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
        
        elif decision == 4: 
            #El usuario eligió a cuatro perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")

        elif decision == 5: 
            #El usuario eligió a cinco perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
        
        elif decision == 6: 
            #El usuario eligió a seis perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
            perfil6 = input("Ingrese el nombre del usuario: ")

        elif decision == 7: 
            #El usuario eligió a siete perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
            perfil6 = input("Ingrese el nombre del usuario: ")
            perfil7 = input("Ingrese el nombre del usuario: ")
        
        elif decision == 8: 
            #El usuario eligió a ocho perfiles.
            perfil1 = input("Ingrese el nombre del usuario: ")
            perfil2 = input("Ingrese el nombre del usuario: ")
            perfil3 = input("Ingrese el nombre del usuario: ")
            perfil4 = input("Ingrese el nombre del usuario: ")
            perfil5 = input("Ingrese el nombre del usuario: ")
            perfil6 = input("Ingrese el nombre del usuario: ")
            perfil7 = input("Ingrese el nombre del usuario: ")
            perfil8 = input("Ingrese el nombre del usuario: ")
    
avanzado()