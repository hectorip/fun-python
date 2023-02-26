from itertools import filterfalse

# filterfalse es como un filto invertido, sólamente deja
# los elementos que no cumplan la condición

nombres = ["Juan", "Pedro", "Luis", "Ana", "María", "Lorena"]

# Encontremos los nombres que no empiezan con "L"

no_l = filterfalse(lambda x: x.startswith("L"), nombres)

for name in no_l:
    print(name)

# ¿Por qué quiero usar filterfalse en vez de filter?
# Cuando la comparación es compleja, filterfalse es más entendible, y ese es el caso
# principal de uso de filterfalse

no_l = filter(lambda x: not (x.startswith("L") or x.startswith("M")), nombres)

for name in no_l:
    print(name)
