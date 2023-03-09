"""
Accumulate

Devuelve un iterador que va acumulando todos los valores anteriores de la secuencia,
muy parecido a reduce, pero haciéndolo de manera progresiva
"""
from itertools import accumulate

valores = [1, 2, 3, 4, 5]

for i in accumulate(valores):
    print(i)

# También puede recibir una función de acumulación

for i in accumulate(valores, lambda x, y: x * y):
    print(i)

