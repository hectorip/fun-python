"""zip_longest
Cuando quieres emparejar dos colecciones pero resulta que no tienen la misma longitud,

"""
from itertools import zip_longest


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10, 11, 12]

# El zip normal corta cuando una de las colecciones se acaba
for i in zip(a, b):
    print(i)

# Zip longest, al contrario, rellena con algún valor que le digas, tomando como
# referencia el valor más largo


for i in zip_longest(a, b, fillvalue=10):
    print(i)

# Esto es muy valioso cuando no sabemos el tamaño de las colecciones
# que vamos a zippear pero queremos ocupar todos los valores en ambas