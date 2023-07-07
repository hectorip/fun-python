from functools import reduce

# El reduce es un tipo de "doblado", va tomando los valores en
# la secuencia y los va aplicando a la función que se le pasa,
# guardando el resultado después de cada aplicación y pasándolo
# como primer argumento en la siguiente aplicación

# Imagina el doblado como tener una tira de papel (tu colección)
# y empezar doblarla por cachitos, reduciendo su tamaño, hasta
# que te queda un solo cachito (el resultado)

# La reducción es un caso específico de doblado, que siempre empieza
# por la izquierda y acumula el valor

numeros = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, numeros))
