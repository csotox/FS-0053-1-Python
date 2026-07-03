#      nombre_modulo
import     sumar

# Util cuando modulo/libreria es muy grande
# para que ocupe menos memoria
#     modulo            Funcion
from  restar    import   restar

def tomar_datos():
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    return x, y


print("Calculadora básica")
print("------------------\n")
print("¿Qué operación le gustaria realizar?")
print("1. Sumar dos números")
print("2. Restar dos números")
print("0. Salir")

opcion = input("> ")

# Realizamos esta refactorización para tener un solo punto
# de ingresos de datos del usuario.
# Más adelante vamos a cambiar la función tomar_datos()
# entonces debemos asegurar tener un solo punto de
# entrada.
if opcion in ("1", "2"):
    x, y = tomar_datos()
    if opcion == "1":
        # Si utilizamos solo import
        # modulo+función
        sumar.sumar(x, y)
    elif opcion == "2":
        # Si importamos con from
        # función
        restar(x, y)
elif opcion == "0":
    print("Nos vemos a la próxima")
else:
    print("No existe la opción solicitada")
