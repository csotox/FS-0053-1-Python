# En la POO tenemos 2 tipos de elementos
# Atributos -> Datos/Estados
# Métodos -> Acciones

"""
Automóvil

Datos:
- Marca
- Modelo
- Color
- Encendido
- Velocidad

Acciones/comportamiento:
- Encender
- Apagar el auto
- Acelerar
- Frenar
- Mostrar info
"""


# Clase - Receta/Plantilla
class Automovil:

    # Constructor
    # self == this
    def __init__(self, marca: str = "NA", modelo: str = "NA", color: str = "NA"):
        # Atributos de identidad
        self.marca = marca
        self.modelo = modelo
        self.color = color
        # atributos de estado
        self.__encendido = False
        self.__velocidad = 0

    def __str__(self):
        return f"Automóvil: {self.marca} {self.modelo} {self.color}"

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Encendido: {self.__encendido}")
        print(f"Velocidad: {self.__velocidad} km/h")

    def encender(self):
        self.__encendido = True
        print("El auto está encendido")

    def apagar(self):
        self.__encendido = False
        print("El auto está apagado")

    def acelerar(self, velocidad: int = 10):
        if velocidad < 0:
            print("La velocidad no puede ser negativa")
        elif self.__encendido:
            self.__velocidad += velocidad
            print(f"El auto aceleró a {self.__velocidad} km/h")
        else:
            print("El auto está apagado, no puede acelerar")

    def frenar(self, velocidad: int = 10):
        if velocidad < 0:
            print("La velocidad no puede ser negativa")
        elif self.__encendido:
            if self.__velocidad - velocidad < 0:
                self.__velocidad = 0
            else:
                self.__velocidad -= velocidad
            print(f"El auto frenó a {self.__velocidad} km/h")
        else:
            print("El auto está apagado, no puede frenar")

    # Getter
    @property
    def velocidad(self):
        return self.__velocidad

    # Setter
    @velocidad.setter
    def velocidad(self, velocidad: int):
        if velocidad < 0:
            print("La velocidad no puede ser negativa")
        elif self.__encendido:
            self.__velocidad = velocidad
            print(f"El auto aceleró a {self.__velocidad} km/h")
        else:
            print("El auto está apagado, no puede acelerar")



# -- - ---------------------------------------------------------
# Objeto / Instancia
auto_1 = Automovil("Toyota", "Corolla", "Rojo")
auto_2 = Automovil()      # Los argumentos del constructor son opcionales y tienen valores por defecto
auto_3 = Automovil(modelo="Civic", marca="Honda", color="Azul")

# print( type(1) )
# print( type(auto_1) )
# print( isinstance(auto_1, Automovil) )

# Cuando utilizamos el constructor, no es necesario asignar los
# valores de los atributos uno por uno
# auto_1.marca = "Toyota"
# auto_1.modelo = "Corolla"
# auto_1.color = "Rojo"

# print(auto_1.marca)
# print(auto_1.modelo)
# print(auto_1.color)
# print(auto_2.marca)
# print(auto_2.modelo)
# print(auto_2.color)
# print(auto_3.marca)
# print(auto_3.modelo)
# print(auto_3.color)

# print()
# print(auto_1)
# print(auto_1.__str__())



# auto_1.__velocidad = 10
# auto_1._Automovil__velocidad = 2000 # type: ignore

# auto_1.mostrar_info()

# print(auto_1.__velocidad)
# print(auto_1._Automovil__velocidad) # type: ignore

# print(auto_1.__dict__)  # Muestra los atributos del objeto


# auto_1.mostrar_info()
# print()
# auto_1.encender()
# print()
# auto_1.mostrar_info()
# print()
# auto_1.apagar()
# print()
# auto_1.mostrar_info()


# auto_1.mostrar_info()
# auto_1.acelerar(-10)
# auto_1.acelerar(5)
# auto_1.encender()
# auto_1.acelerar(5)
# auto_1.acelerar(10)
# auto_1.acelerar(15)
# auto_1.frenar(15)
# auto_1.frenar(45)

auto_1.encender()
auto_1.acelerar(5)
auto_1.acelerar(10)
print( auto_1.velocidad )   # getter

auto_1.velocidad = 20       # setter
print( auto_1.velocidad )

