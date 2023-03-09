"""zip_longest
Cuando quieres emparejar dos colecciones pero resulta que no tienen la misma longitud,

"""

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10, 11, 12]

# El zip normal corta cuando una de las colecciones se acaba
for i in zip(a, b):
    print(i)