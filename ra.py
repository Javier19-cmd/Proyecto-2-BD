import random
import cryptocode

#Encriptando contraseña.
passkey = 'UVG' #Llave para encriptar.

contraseña = "Ctkh+dE=*L9B8Q6RaprHA67FEfruFCA==*aOfAN/I9Zcrqwac/M+tdiA==*j8InvuoXCnm7gOvsQ0/niQ=="

conn = cryptocode.decrypt(contraseña, passkey) #Contraseña encriptada.

print(conn)