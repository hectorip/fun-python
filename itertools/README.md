# Itertools

Te permitirá crear y trabajar con iteradores al más puro estilo de lenguajes funcionales como Haskell o APL.

## ¿Qué es un iterador?

Un iterador es un objeto que permite recorrer una secuencia de elementos. En Python, los iteradores son objetos que implementan el método `__next__` que devuelve el siguiente elemento de la secuencia. Cuando no hay más elementos, se lanza la excepción `StopIteration`.

Un iterador tiene un estado interno que permite calcular qué devolverá en la siguiente llamada. Dependiendo de cómo se usen te pueden ayudar a ahorrar memoria. También te permiten crear secuencias infinitas, lo cuál es imposible con las listas.

Si la colección es muy grande y los valores se pueden calcular algorítmicamente, entonces te conviene crear un iterador en lugar de una lista.
