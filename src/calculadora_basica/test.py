from sumar import sumar
from restar import restar

# Sumar envio dos números enteros
resp = sumar(10, 20)
if resp == 30:
    print(".", end="")
else:
    print("E", end="")

# Sumar envio de un entero y una cadena
try:
    resp = sumar(10, "20") # type: ignore
    print("E", end="")
except:
    print(".", end="")

# Restar envio dos números enteros
resp = restar(10, 20)
if resp == -10:
    print(".", end="")
else:
    print("E", end="")

# restar envio de un entero y una cadena
try:
    resp = restar(10, "20") # type: ignore
    print("E", end="")
except:
    print(".", end="")

print()
