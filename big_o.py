def f(n):
    for i in  range(n):
        print(i)
    
    for i in range(i):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n) -> la función crece en O de n, porque la n es la que pesa más


def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n * n):
        print(i)
    
# O(n) + O(n * n) = O(n + ncuadrado) = O(ncuadrado) -> crece en función de n cuadrado porque es la variable que más peso tiene 

# Ley de la multiplicación

def f(n):
    for i in range(n):

        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n * n) = O(ncuadrado) -> crece de manera cuadrática

# Recursividad múltiple

def fibonacci(n):
    if n == 0 or n == 1:
        return
    
    return fibonacci(n-1) + fibonacci(n-2)

# O(2**n) -> por cada llamada de fibonacci hago dos llamadas, 2 por cada vez que tenemos n, crecimiento exponencial