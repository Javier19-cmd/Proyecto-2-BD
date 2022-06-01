#Importando los datos de la BD.
from datos import * 
#Librería para la base de datos.
import psycopg2 

def connect():
  #Conexión a la base de datos.
  conn = psycopg2.connect(host=host(), user=user(), password=passw(), port=port(), database=BD())
  return conn

def disconnect(conn):
  conn.close()

def setConnection(conn):
  global connection
  connection = conn

def getConnection():
  return connection