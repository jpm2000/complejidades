def f(x):

    # Asignación 

    respuesta = 0

    # No importa el tamaño de x, va a correr 1000 veces el loop

    for i in range(1000):
        respueta += 1
    
    # Si importa cuanto es x para que el loop corra

    for i in range(x):
        respuesta += x

    # Loop que esta dentro de un loop. x*x=xcuadrada=2xcuadrada
    
    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1
    
    # Esto es un polinomio y la variable que pesa es la constante, x cuadrada pesa cada vez más

    return respuesta

