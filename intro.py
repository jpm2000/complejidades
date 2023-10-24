import time

'''
Voy a hacer dos implementaciones de factoriales
Para poder medir, predecir y comparar

Para medir el tiempo

Voy a hacer una comparación entre una implementación recursiva e iterativa
Predecir cual va a ser el comportamiento según vaya creciendo la complejidad
'''

# Factorial iterativo

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta = respuesta * n
        # lo puedo escribir respuesa *= n
        n -= 1

    return respuesta

# Factorial recursivo

'''
def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)
'''
def factorial_r(n):
    # Caso base
    if n == 1:
        return 1
    
    return n * (n - 1)

if __name__ == '__main__':
    n = 10000000000

    # ejecuto el modulo time que tiene una funcion que se llama time
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)


'''
import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
'''