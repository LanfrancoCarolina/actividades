
# fizzbuzz.py

#class FizzBuzz:
    #def __init__(self, num):
        #self.num = num

    #def convert_to_fizzbuzz(self):
     #if self.num % 15 == 0:   # múltiplo de 3 y 5
       # return "FizzBuzz"
    # elif self.num % 3 == 0:
        #return "Fizz"
     #elif self.num % 5 == 0:
        #return "Buzz"
    # return str(self.num)
    

#Este seria el codigo refactorizado mas limpio y claro
class FizzBuzz:
     def __init__(self, num):
        self.num = num

     def convert_to_fizzbuzz(self):
        """
        Convierte un número a su representación FizzBuzz:
        - Múltiplo de 3 → "Fizz"
        - Múltiplo de 5 → "Buzz"
        - Múltiplo de ambos → "FizzBuzz"
        - Otros → el número como string
        """
        result = ""
        if self.num % 3 == 0:
            result += "Fizz"
        if self.num % 5 == 0:
            result += "Buzz"
        return result or str(self.num)