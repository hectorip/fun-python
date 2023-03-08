"""
Permutations

Permutaciones de un iterable, de tamaño definido o del iterable completo

"""
from itertools import permutations

elementos = [1, 2, 3, 4, 5]

# Permutaciones de tamaño 2

permutaciones = permutations(elementos, 2)

for p in permutaciones:
    print(p)

# Esta función es muy útil porque las permutaciones pueden crecer muy rápido.