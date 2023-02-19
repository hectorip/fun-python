
from itertools import count
import time
"""
¿Cómo harías una secuencia infinita de números en Python?
Una forma es hacer un while con un contador, pero hay una forma más elegante:

itertools.count(start=0, step=1)
Es parecido a range, pero no tiene límite superior, además NO ES UNA LISTA, es un iterador,
por lo que no ocupa mucha memoria.
"""

# Esto correrá infinitamente
counter = count()
while True:
    print(next(counter))
    # Esperamos un segundo para no ver una lista de números corriendo como locos
    time.sleep(1)

# Pero el for lo hace automáticamente por nosotros

for i in count():  # For llama automáticamente a next()
    print(i)
    time.sleep(1)
