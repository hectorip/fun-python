# Generadores
# Un generador es una función que cuando se llama
# devuelve un objeto iterable. Este objeto
import time
def pares(n=None):
    i = -2
    if n is None:
        while True:
            i += 2
            # yield es como return, pero le indica al intérprete que esta
            # función no se puede desechar, se guarda el estado y la próxima vez que se llame la función corre a partir de aquí
            yield i
    else:
        while i >= n:
            i += 2
            yield i

par = pares()
print(par)

for i in par:
    print(i)
    time.sleep(0.2)