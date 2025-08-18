
class Carta:
    def __init__(self,valor,palo):
        self.valor = valor
        self.palo = palo
        
    def __str__(self):
        return f" Tu carta es el {self.valor} de {self.palo}"
    def __getitem__(self,index):
        if index == 0:
         return f" Tu carta es el: {self.valor}"
        elif index == 1:
           return f" Tu carta es del palo: {self.palo}"
        else:
           raise IndexError("Índice inválido. Use 0 para valor o 1 para palo.")
        


        
carta1 = Carta(4,"copa")
print(carta1)        
print(carta1[0])      
print(carta1[1])              