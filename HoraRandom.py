#Referencia: https://stackoverflow.com/questions/26740227/create-random-time-stamp-list-in-python
from random import randrange
import datetime 
import random

def random_date(start,l): #Función que genera las horas aleatorias.
   current = start
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(60))
      yield curr
      l-=1

hora = random.randint(1, 24) #Generando hora random.
mins = random.randint(0,60)  #Generando minutos random.
año = int(input("Ingrese el año "))
mes = int(input("Ingrese el mes "))
dia = int(input("Ingrese el día "))

startDate = datetime.datetime(año,mes,dia,hora,mins) #Variable que guarda la fecha y la hora.

for x in random_date(startDate,8000): #For que genera las horas.
  print(x.strftime("%d/%m/%y %H:%M:%S"))