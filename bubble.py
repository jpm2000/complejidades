import random

def ordenamiento(lista):
    # Iterar a lo largo de la lista y cada vez un poco menos, porque garantizaremos que estan ordenados los elementos
    n = len(lista)

    for i in range(n):

        # Es menos 1 porque estamos tomando longitudes 
        for j in range(0, n - i - 1): # Crecimiento cuadrático O(n**n) O(n cuadrada)
            
            # Comparando los elementos adyacentes 
            if lista[j] > lista[j + 1]:
                
                #Swapping 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

if __name__ == '__main__':
    tamaño_lista = int(input('De que tamaño será la lista? '))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print(lista)

    ordenada = ordenamiento(lista)
    print(ordenada)

    '''
    import random


def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
    '''