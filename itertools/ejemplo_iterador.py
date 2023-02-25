import time

class Pares:
    """Devuelve todos los pares menores o iguales a n"""
    def __init__(self, n=None):
        self.max = n
        print("Se ha llamado a __init__")

    def __iter__(self):
        self.n = -2
        print("Se ha llamado a __iter__")
        return self

    def __next__(self):
        self.n += 2
        if self.max is None:
            return self.n
        if self.n >= self.max:
            raise StopIteration
        return self.n


for i in Pares(): # no existe una lista de 100 elementos, sólo se crea un elemento a la vez
    print(i)
    time.sleep(0.2)
