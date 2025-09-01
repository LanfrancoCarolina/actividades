
#def test_fizzbuzz_1():
    #my_fizzbuzz = FizzBuzz(1)
    #assert my_fizzbuzz.convert_to_fizzbuzz() == "1"
#def test_fizzbuzz_2():
   # my_fizzbuzz = FizzBuzz(2)
   # assert my_fizzbuzz.convert_to_fizzbuzz() == "2"
#def test_fizzbuzz_fizz():
   # my_fizzbuzz = FizzBuzz(3)
    #assert my_fizzbuzz.convert_to_fizzbuzz() == "Fizz"
#def test_fizzbuzz_buzz():
    #my_fizzbuzz = FizzBuzz(5)
    #assert my_fizzbuzz.convert_to_fizzbuzz() == "Buzz"
#def test_fizzbuzz_fizzbuzz():
    #my_fizzbuzz = FizzBuzz(15)
    #assert my_fizzbuzz.convert_to_fizzbuzz() == "FizzBuzz"

# test_fizzbuzz.py Una sola función cubre todos los casos importantes.

#Fácil de agregar nuevos casos si querés probar más números.
import pytest
from fizzbuzz import FizzBuzz

@pytest.mark.parametrize("num, esperado", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (6, "Fizz"),
    (10, "Buzz")
])
def test_fizzbuzz(num, esperado):
    assert FizzBuzz(num).convert_to_fizzbuzz() == esperado
