TITULO = "Pizza JAT"
COLUMNAS = 30

ingredientes = set()

# Ingredientes
def menu():
    print("1. Tomate")
    print("2. Champiñones")
    print("3. Aceitunas")
    print("4. Cebolla")
    print("5. Pollo")
    print("6. Jamón")
    print("7. Carne")
    print("8. Tocino")
    print("9. Queso")
    print("10. Listo!")

# Refactorizado
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

# Refactorizado
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

# Tipo de ingredientes
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

def quitar_ing():
    op = 1
    while op != 10:
        print("---------")
        print("Los ingredientes de su pizza son :")
        print("---------")
        for i in ingredientes:
            print(i)
        print("---------")
        print("¿Que ingredientes desea eliminar?")
        print("---------")
        menu()
        print("---------")
        try:
            op = int(input("Su opcion: "))
            if op == 1:
                ingredientes.discard("Tomate")   
            elif op == 2:
                ingredientes.discard("Champiñones")
            elif op == 3:
                ingredientes.discard("Aceitunas") 
            elif op == 4:
                ingredientes.discard("Cebolla")
            elif op == 5:
                ingredientes.discard("Pollo")
            elif op == 6:
                ingredientes.discard("Jamón")
            elif op == 7:
                ingredientes.discard("Carne")
            elif op == 8:
                ingredientes.discard("Tocino")
            elif op == 9:
                ingredientes.discard("Queso")
            elif op == 10:
                print("Volviendo a seleccion de ingredientes...")
                print("---------") 
            else:
                print("Ingrese valores del menu")

        except ValueError:
            print("Ingrese solo numeros")  

def tiempo():

    t= 20 + (2 * len(ingredientes))
    return t

def pizza():
    print("---------")
    print(f"Su {titulo} de {masa} con {salsa} tiene: ")
    print("---------")
    for i in ingredientes:
        print(i)

def menu_4():
    opp = 0
    while opp != 3:
        print("---------")
        print(f"El tiempo estimado para su pizza es de {tiempo()} min.")
        print("---------")
        print("¿Acepta el pedido?")
        print("1. Ver ingredientes")
        print("2. No")
        print("3. Sí")
        print("---------")
        try:
            opp = int(input("Su opcion: "))
            if opp == 1:
                pizza()
            elif opp == 2:
                menu_3()
            elif opp == 3:
                print("Su pedido se está preparando...")
            else:
                print("Ingrese valores del menu")

        except ValueError:
            print("Ingrese solo numeros")
    return TITULO

def menu_opciones(tipo_masa, tipo_salsa, tipo_ingre):

    if tipo_masa != '' or tipo_salsa != '' :
        print("Ingredientes seleccionados")
        print(f"Tipo de masa: {tipo_masa}" )
        print(f"Tipo de salsa: {tipo_salsa}" )
        print(f"Ingredientes: {tipo_ingre}" )
        print()

    print("Seleccione una opción")
    print("1. Tipo de masa")
    print("2. Tipo de salsa")
    print("3. Agregar ingredientes")
    print("4. Cerrar pedido")
    print("0. Salir")

    opcion = input("> ")

    return opcion


def menu_principal():

    opcion = ''
    tipo_masa = ''
    tipo_salsa = ''
    tipo_ingre = set()
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


def main():
    menu_principal()

if __name__ == '__main__':
    main()
