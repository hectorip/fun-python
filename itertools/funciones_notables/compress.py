from itertools import compress

# Compres sirve para escoger los elementos de una lista basado en otra lista paralela


# Ejemplo: Imagina que tienes que reportar las asistencias de un grupo
# de personas. Tienes una lista con los nombres de las personas
# y un matriz con las asistencias de los días de la semana, de la sigeuiente forma:

nombres = ["Juan", "Pedro", "Luis", "Ana", "María", "Lorena"]
asistencias = {
    "Lunes": [True, True, True, False, False, False],
    "Martes": [True, True, False, False, False, False],
    "Miércoles": [True, True, True, True, True, True],
    "Jueves": [False, False, False, False, False, False],
    "Viernes": [True, False, True, False, True, False],
}

# Quieres saber quién asisitió un día específico.
# Con compress puedes crear una función así:


def asistencias_dia(dia):
    return list(compress(nombres, asistencias[dia]))


# Y ahora puedes usarla así:
print(asistencias_dia("Lunes"))
