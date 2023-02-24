import time

class Pares:
    """Devuelve todos los pares menores o iguales a n"""
    def __init__(self, n):
        self.max = n
        print("Se ha llamado a __init__")

    def __iter__(self):
        self.n = -2
        print("Se ha llamado a __iter__")
        return self

    def __next__(self):
        if self.n >= self.max:
            raise StopIteration
        self.n += 2
        return self.n



    #for i in range(0, n + 1, 2):
    #    yield i # yield es como return, pero le indica al intérprete que esta función no se puede desechar, se guarda el estado y la próxima vez que se llame la función corre a partir de aquí

for i in Pares(100): # no existe una lista de 100 elementos, sólo se crea un elemento a la vez
    print(i)
    time.sleep(0.2)
