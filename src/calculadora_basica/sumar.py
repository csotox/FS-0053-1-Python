# esta sintaxis de: int | float
# indica que puede recibir uno
# de estos tipos de datos
def sumar(x: int | float, y: int):
    """
    fx que suma dos números
    """
    # Al sacar el print() de la función y retornar
    # el resultado de la suma, ahora la función
    # cumple con responsabilidad unica
    return x + y
