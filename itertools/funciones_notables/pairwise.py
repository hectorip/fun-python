"""
Pairwise

A veces necesitamos iterar sobre dos elementos a la vez en secuencias entrelazadas,
es decir, el segundo elemento de un par debe ser el primer elemento
del siguiente. Esto es lo que hace pairwise.

"""

from itertools import pairwise

pares = pairwise([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for (i, j) in pares:
    print(i, j)
    print(i + j)

# Hay algoritmos que requieren esto, por ejemplo, imagínate que quieres encontrar
# la suma más grande de dos elementos consecutivos en una lista.

def max_consecutive_sum(numbers):
    return max(a + b for a, b in pairwise(numbers))

print("MAX consecutive sum:", max_consecutive_sum([1, 2, 3, 4,20,  5, 6, 7, 8, 9, 10]))