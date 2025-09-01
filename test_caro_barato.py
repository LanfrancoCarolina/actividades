
# test_caro_barato.py
import pytest
from caro_barato import evaluar_precio

@pytest.mark.parametrize("precio, cantidad, esperado", [
    (0, 5, "¿Fue gratis, o no compraste nada?"),  # precio 0
    (120, 1, "Caro"),                             # producto caro
    (20, 5, "Barato"),                             # producto barato
    (0, 0, "¿Fue gratis, o no compraste nada?"),   # precio y cantidad 0
    (60, 5, "Caro"),                               # precio > 50 y cantidad < 10
    (50, 10, "Barato")                             # precio ≤ 50 y cantidad ≥ 10
])
def test_evaluar_precio(precio, cantidad, esperado):
    assert evaluar_precio(precio, cantidad) == esperado