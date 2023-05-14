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

# Esta función es muy útil porque las permutaciones pueden crecer muy rápido,
# así que al tenerlas como un iterador, podemos empezar a trabajar con ellas,
# primero sin hacerlo nosotros mismos y segundo, sin ocupar un montón de memoria
# además de que tenemos la posibilidad de hacer permutaciones de tamaño arbitrario
