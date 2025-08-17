
class Moneda:
    tasa_de_conversion = {'USD':1,
                          'ARS':1270

    }
    def __init__(self,cantidad,divisa):
        self.cantidad = cantidad
        self.divisa = divisa
    def convertir_a(self,otra_divisa):
        tasa_actual = Moneda.tasa_de_conversion[self.divisa]
        tasa_destino = Moneda.tasa_de_conversion[otra_divisa]
        cantidad_convertida = self.cantidad * tasa_destino/tasa_actual
        return Moneda(cantidad_convertida,otra_divisa)
    def __str__(self):
        return f"{self.cantidad} {self.divisa}"
    def __add__(self,otra_moneda):
        moneda_convertida = otra_moneda.convertir_a(self.divisa)
        cantidad_total = self.cantidad + moneda_convertida.cantidad
        return Moneda(cantidad_total,self.divisa)
    
dolares = Moneda(10, "USD")   # 10 dólares
pesos = Moneda(20000, "ARS") # 1270 pesos


convertidor = pesos.convertir_a("USD")
print(convertidor) 






    
    
    
    
    

        