# esta sintaxis de: int | float
# indica que puede recibir uno
# de estos tipos de datos
def sumar(x: int | float, y: int):
    """
    fx que suma dos números
    """
    print( f"El resultado de la suma es: {x + y}")
