from itertools import cycle, count
import time
# cycle permite iterar sobre una secuencia infinitamente, repitiéndola


for i in cycle([1, 2, 3]):
    print(i)
    time.sleep(1)
    break

# 1, 2, 3, 1, 2, 3, 1, 2, 3, 1...

# cycle acepta cualquier tipo de iterador, no sólo listas

for i in cycle(range(10)):
    print(i)
    time.sleep(0.2)
    break
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4...


for i in cycle("HOLA"):
    print(i)
    time.sleep(0.2)
    break
 # H, O, L, A, H, O, L, A, H, O, L, A, H...

 # Qué pasa si le pasamos un iterador vacío? No produce nada

for i in cycle([]):
    print(i)
    time.sleep(1)

# Vamos a combinarlo con count mediante zip

for i in zip(count(), cycle("HOLA")):
    print(i)
    time.sleep(0.2)
    break
# Ahora tenemos una secuencia infinita de tuplas
