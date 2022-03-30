import random
import cryptocode

#Desencriptar las contraseñas.
passkey = 'UVG' #Llave para encriptar.

#Usuario de Roberto.
contraseña = "Ctkh+dE=*L9B8Q6RaprHA67FEfruFCA==*aOfAN/I9Zcrqwac/M+tdiA==*j8InvuoXCnm7gOvsQ0/niQ=="

conn = cryptocode.decrypt(contraseña, passkey) #Contraseña encriptada.

print(conn)

#Usuario de Juan (cuenta comercial)
passkey = 'UVG' #Llave para encriptar.

#Usuario de Roberto.
contraseña = "1FVCfbk=*UZw4MqzQv8RdEPpZFK+UJg==*KALuAlWCwEeiaVOzTBTeqg==*tUukpaUeKavsN9C+9toDqg=="

conn = cryptocode.decrypt(contraseña, passkey) #Contraseña encriptada.

print(conn)