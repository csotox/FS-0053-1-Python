# v0.0.0
# Historia de usuario:
"""
El usuario necesita el cálculo del área de un rectángulo.
A partir de ingresar la base y la altura
"""

base = input( "Ingrese la base del rectángulo: ")
altura = input( "Ingrese la altura del rectángulo: ")

if base.isdigit() and altura.isdigit():
    area = int( base ) * int( altura )
    print( f"El área del rectángulo es: {area}" )
else:
    print( "ERROR" )
    print( "Los valores ingresados deben ser número enteros" )
    print( f"Valores ingresados Base: {base} - Altura: {altura}" )
