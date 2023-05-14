"""Accumulate

    Devuelve un iterador que va acumulando todos los valores anteriores de la secuencia.
    Por defecto, la función de acumulación es la suma, pero se puede pasar una función de acumulación.
"""

from itertools import accumulate

acumulados = accumulate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

for i in acumulados:
    print(i)

# También acepta una función de acumulación

factoriales = accumulate(range(1, 1000), lambda x, y: x * y)

for i in factoriales:
    print(i)
