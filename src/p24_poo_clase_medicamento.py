class Medicamento():
    descuento = 0.05
    IVA = 0.18
    precio = 0

    @staticmethod
    def validar_mayor_a_cero(numero: int) -> bool:
        return (numero > 0)

    @staticmethod
    def cal_descuento(precio: int) -> float:
        if precio >= 10_000 and precio < 20_000:
            descuento = 0.1
        elif precio >= 20_000 and precio < 30_000:
            descuento = 0.2
        elif precio >= 30_000:
            descuento = 0.3
        else:
            descuento = 0.0

        return descuento

    def asignar_precio(self, precio_entregado: int) -> None:

        if self.validar_mayor_a_cero(precio_entregado):
            self.precio = precio_entregado

            # Definir descuento
            self.descuento = self.cal_descuento(precio_entregado)

        else:
            print( f"El precio: {precio_entregado} no es un precio valido" )
