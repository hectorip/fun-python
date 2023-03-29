import time

"""
Generadores

Un generador es una función que cuando se llama
devuelve un objeto iterable. Cada que se llama a la función
next() sobre este iterable, la función se ejecuta hasta que
encuentra un `yield` que es como un return, pero pausa
la ejecución de la función y guarda su estado hasta la próxima
llamada a next(). La función continua su ejecución desde
donde se quedó.
"""


def pares(n=None):
    i = -2  # el primer par es 0
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
