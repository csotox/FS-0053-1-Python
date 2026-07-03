def sumar(x, y):
    print( f"El resultado de la suma es: {x + y}")

def restar(x, y):
    print( f"El resultado de la resta es: {x - y}")

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
        sumar(x, y)
    elif opcion == "2":
        restar(x, y)
elif opcion == "0":
    print("Nos vemos a la próxima")
else:
    print("No existe la opción solicitada")



# Tipado de int y float
