# Código orginal: src/sumar-dos-numeros.py
# Hacemos que trabaje con funciones

numero1 = input("Ingrese el primer número entero:")
numero2 = input("Ingrese el segundo número entero:")

if numero1.isdigit() and numero2.isdigit():
    numero_1 = int(numero1)
    numero_2 = int(numero2)

    suma = numero_1 + numero_2

    print(f"La suma de los números es: {suma}")
else:
    print("Error!!!!")
    print("Los valores ingresados deben ser números enteros")
    print(f"Primer número es: {numero1} y segundo número es: {numero2}")
