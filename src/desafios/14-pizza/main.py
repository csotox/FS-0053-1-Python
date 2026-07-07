TITULO = "Pizza JAT"
COLUMNAS = 30

def menu_masa():
    print("Tipo De Masa")
    print("1. Masa tradicional")
    print("2. Masa delgada")
    print("3. Masa con bordes de queso")
    print("---------")
    op1 = 0
    while op1 not in range(1,4):
        tipo = ''
        try:
            op1 = int(input("Ingrese opcion: "))
            if op1 == 1:
                tipo = "Masa tradicional"
            elif op1 == 2:
                tipo = "Masa delgada"
            elif op1 == 3:
                tipo = "Masa con bordes de queso"
            else:
                print("Opcion invalida")
                print("---------")
        except ValueError:
            print("Ingrese solo numeros")

    return tipo

def menu_salsa():
    salsas = {
        "1": "Salsa de tomate",
        "2": "Salsa alfredo",
        "3": "Salsa barbecue",
        "4": "Salsa pesto",
    }

    print("Tipo De Salsa")
    for c, v in salsas.items():
        print( f"{c}. {v}")

    op2 = ""
    while op2 != '0':
        op2 = input("Ingrese opcion: ")
        salsa = salsas.get(op2, None)

        if salsa:
            break
        elif op2 == '0':
            break
        else:
            print("Opcion invalida debe seleccionar una opción del menú")
            print("---------")

    return salsa

def menu_ingredientes(tipo_ingre: set):
    lista_ingre = {
        '1': 'Tomate',
        '2': 'Champiñones',
        '3': 'Aceitunas',
        '4': 'Cebolla',
        '5': 'Pollo',
        '6': 'Jamón',
        '7': 'Carne',
        '8': 'Tocino',
        '9': 'Queso'
    }

    op3 = ''
    while op3 != '0':
        print("Tipo de ingredientes")
        for c, v in lista_ingre.items():
            print( f"{c}. {v}")
        print( "0. Salir")

        op3 = input("Ingrese opcion: ")
        ing = lista_ingre.get(op3, None)

        if ing:
            tipo_ingre.add(ing)
            continue
        elif op3 == '0':
            break
        else:
            print("Opcion invalida debe seleccionar una opción del menú")
            print("---------")

    return tipo_ingre

def menu_eliminar_ingredientes(tipo_ingre: set):
    op = ''
    lista = list(tipo_ingre)
    while op != '0':
        print("Seleccione el ingrediente a eliminar")
        for i, v in enumerate(lista):
            print( f"{i+1}. {v}")
        print( "0. Salir")

        op = input("Ingrese opcion: ")

        if op == '0':
            break

        try:
            # UX para facilitar la selección no utilizamos
            # el cero para eliminar el elemento.
            # Mantenemos el cero para salir del menú
            opcion = int(op) - 1
            ing = lista.pop(opcion)
        except ValueError:
            print("Opción invalida debe seleccionar una opción del menú")
            print("---------")

    return set(lista)

def tiempo(tipo_ingre):

    t = 20 + (2 * len(tipo_ingre))
    return t

def pizza(tipo_masa, tipo_salsa, tipo_ingre):
    print("-------------------------------------------------------")
    print("Su pedido es:\n")
    print(f"Su {TITULO} de {tipo_masa} con {tipo_salsa} tiene: ")
    for i in tipo_ingre:
        print(i)
    print()
    print(f"Sera despachada en: {tiempo(tipo_ingre)} min")
    print("-------------------------------------------------------")

    op = input("Desea confirmar el pedido [S/N] ")

    return op

def menu_opciones(tipo_masa, tipo_salsa, tipo_ingre):

    if tipo_masa != '' or tipo_salsa != '' :
        print("Ingredientes seleccionados")
        print(f"Tipo de masa: {tipo_masa}" )
        print(f"Tipo de salsa: {tipo_salsa}" )
        print(f"Ingredientes: {tipo_ingre}" )
        print(f"Tiempo estimado : {tiempo(tipo_ingre)} min" )
        print()

    print("Seleccione una opción")
    print("1. Tipo de masa")
    print("2. Tipo de salsa")
    print("3. Agregar ingredientes")
    print("4. Eliminar ingredientes")
    print("5. Cerrar pedido")
    print("0. Salir")

    opcion = input("> ")

    return opcion

def inicializar():
    return '', '', set()

def menu_principal():

    opcion = ''
    tipo_masa, tipo_salsa, tipo_ingre = inicializar()
    while opcion != '0':
        print( f"{'Bienvenidos/as':^{COLUMNAS}}" )
        print(f"{TITULO:^{COLUMNAS}}")
        print("=" * COLUMNAS, "\n")

        opcion = menu_opciones(tipo_masa, tipo_salsa, tipo_ingre)

        if opcion == '1':
            tipo_masa = menu_masa()
        elif opcion == '2':
            tipo_salsa = menu_salsa()
        elif opcion == '3':
            tipo_ingre = menu_ingredientes(tipo_ingre)
        elif opcion == '4':
            tipo_ingre = menu_eliminar_ingredientes(tipo_ingre)
        elif opcion == '5':
            op = pizza(tipo_masa, tipo_salsa, tipo_ingre)

            # Se imprime la comanda
            # Se limpian las variables
            if op.lower() == "s":
                tipo_masa, tipo_salsa, tipo_ingre = inicializar()

def main():
    menu_principal()

if __name__ == '__main__':
    main()
