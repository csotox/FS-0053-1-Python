from p24_poo_clase_medicamento import Medicamento

resp = Medicamento()

print()

resp.asignar_precio(-1)
if resp.precio == 0 and resp.descuento == 0.05:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(5_000)
if resp.precio == 5_000 and resp.descuento == 0.0:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(11_000)
if resp.precio == 11_000 and resp.descuento == 0.1:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(25_000)
if resp.precio == 25_000 and resp.descuento == 0.2:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(35_000)
if resp.precio == 35_000 and resp.descuento == 0.3:
    print(".", end="")
else:
    print("E", end="")

if resp.cal_descuento(35_000) == 0.3:
    print(".", end="")
else:
    print("E", end="")

if resp.cal_descuento(19_999) == 0.1:
    print(".", end="")
else:
    print("E", end="")

print()
