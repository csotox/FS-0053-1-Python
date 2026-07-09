class Medicamento():
    descuento = 0.05
    IVA = 0.18
    precio = 0

    @staticmethod
    def validar_mayor_a_cero(numero: int) -> bool:
        return (numero > 0)

    def asignar_precio(self, precio_entregado: int) -> None:
        es_valido = self.validar_mayor_a_cero(precio_entregado)

        if es_valido:
            self.precio = precio_entregado

            # Definir descuento
            self.descuento = 0.0

            if self.precio >= 10_000 and self.precio < 20_000:
                self.descuento = 0.1
            elif self.precio >= 20_000 and self.precio < 30_000:
                self.descuento = 0.2
            elif self.precio >= 30_000:
                self.descuento = 0.3

        else:
            print( f"El precio: {precio_entregado} no es un precio valido" )
