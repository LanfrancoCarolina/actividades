
class NumMayor:
    def __init__(self,*args):
        self.args = args
    def calcular_mayor(self):
        mayor = self.args[0]
        for n in self.args[1:]:
            if n > mayor:
                mayor = n
        return mayor    


if __name__ == "__main__":   
 Num_mayor = NumMayor(3,6,8,10)
 print(Num_mayor.calcular_mayor())


        