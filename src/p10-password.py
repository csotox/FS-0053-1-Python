# getpass es una librería de la biblioteca estandar de Python
import getpass

PASS_BBDD = "hola mundo"     # Esto debe estar encriptado

# Para trabajar con password es mala práctica utilizar
# input() debido a que podemos ver la clave que
# estamos ingresando
#password = input("Ingrese la clase secreta: ")
password = getpass.getpass("Ingrese la clase secreta: ")

while password != PASS_BBDD:
    password = getpass.getpass("Ingrese la clase secreta: ")

print( "Clave correcta. Puede utilizar el programa" )
