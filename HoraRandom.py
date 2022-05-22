#Referencia: https://stackoverflow.com/questions/26740227/create-random-time-stamp-list-in-python
from random import randrange
import datetime 
import random

#Función generadora aleatoria de horas.
def random_date(start,l): #Función que genera las horas aleatorias.
   current = start #Fecha con la que se va a empezar a generar aleatoriamente las horas.
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(60)) #Generando una hora aleatoria
      yield curr #Retornando cada una de las horas generadas.
      l-=1 #Diferencia entre minutos.

"""
#Sección para pedir datos y generar números aleatorios.
hora = random.randint(1, 24) #Generando hora random.
mins = random.randint(0,60)  #Generando minutos random.
año = int(input("Ingrese el año "))
mes = int(input("Ingrese el mes "))
dia = int(input("Ingrese el día "))

startDate = datetime.datetime(año,mes,dia,hora,mins) #Variable que guarda la fecha y la hora.

for x in random_date(startDate,8000): #For que genera las horas.
  z = x.strftime("%Y-%m-%d %H:%M:%S")
  print(z)
"""