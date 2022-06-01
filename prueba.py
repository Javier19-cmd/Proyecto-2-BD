from datos import * #Importando los datos de la BD.
import psycopg2     #Importando la librería de la BD.
import random
import datetime
from HoraRandom import *


año = 2022
mes = 5
dia = 6



#print(startDate)

for i in range(100):
    #Horas aleatorias.
    hora = random.randint(0,23)
    mins = random.randint(0, 59)
    startDate = datetime.datetime(año, mes, dia, hora, mins)

    
    print(startDate)