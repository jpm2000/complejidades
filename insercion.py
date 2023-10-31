import random 

def insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i

        while posicion > 0 and lista[posicion -1] > valor_actual:
            lista[posicion] = lista[posicion -1]
            posicion -= 1
        
        lista[posicion] = valor_actual
    return lista

if __name__ == '__main__':
    tamaño_lista = int(input('De que tamaño será la lista? '))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print(lista)

    ordenada = insercion(lista)
    print(ordenada)

'''
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
'''