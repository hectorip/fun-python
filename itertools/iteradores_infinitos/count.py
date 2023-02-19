

"""
¿Cómo harías una secuencia infinita de números en Python?
Una forma es hacer un while con un contador, pero hay una forma más elegante:

itertools.count(start=0, step=1)
Es parecido a range, pero no tiene límite superior, además NO ES UNA LISTA, es un iterador.
"""

