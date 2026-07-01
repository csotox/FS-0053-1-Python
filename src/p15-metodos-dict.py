print()
print("Agregar elementos a un diccionario (dict)")
print("-----------------------------------------")

# Cuando hacemos referencia a la clave de un dict
# que no existe, la agrega

diccionario = {"llave 1": 5}

print(diccionario)

diccionario["llave 2"] = 9

print(diccionario)

print()
print("Cambiar valor de una clave de un diccionario (dict)")
print("---------------------------------------------------")

diccionario["llave 2"] = 18

print(diccionario)

print()
print("Eliminar elementos")
print("------------------")

diccionario = {
    "celular": 140000,
    "notebook": 489990,
    "tablet": 120000,
    "cargador": 12400,
}
print("Diccionario original", diccionario)

# Método pop()
# Elimina un elemento de un dict usando la clave `key`
# y devuelve el valor de dicho elemento
valor_eliminado = diccionario.pop("celular")
print(" - Eliminado 'celular", diccionario)
print(f"Valor de 'celular' = {valor_eliminado}")

print()
print("Actualizar diccionarios")
print("-----------------------")

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
diccionario_b = {"mascota": "miti", "ejercicio": "bicicleta"}

diccionario_a.update(diccionario_b)

print("Diccionario actualizado", diccionario_a)

diccionario_c = {"edad": 40}
diccionario_a.update(diccionario_c)

print("Diccionario actualizado", diccionario_a)
