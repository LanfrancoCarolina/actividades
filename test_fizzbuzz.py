# test_fizzbuzz.py
from fizzbuzz import FizzBuzz

def test_fizzbuzz_1():
    my_fizzbuzz = FizzBuzz(1)
    assert my_fizzbuzz.convert_to_fizzbuzz() == "1"