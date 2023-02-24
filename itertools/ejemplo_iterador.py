import time
def pares(n):
    """Devuelve todos los pares menores o iguales a n"""
    for i in range(0, n + 1, 2):
        yield i # yield es como return, pero le indica al intérprete que esta función no se puede desechar, se guarda el estado y la próxima vez que se llame la función corre a partir de aquí

for i in pares(100): # no existe una lista de 100 elementos, sólo se crea un elemento a la vez
    print(i)
    time.sleep(0.2)