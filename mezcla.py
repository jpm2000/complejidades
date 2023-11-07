import random

# Creo una función que toma una lista desordenada como input
def mezcla(lista):
    # Sub dividir la lista en lo más pequeñas, tiene un crecimiento logaritmico, se vuelve mas pequeño
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print('listas divididas')
        print(izquierda, ' ', derecha)
        print('')

        #llamada recursiva en cada mitad. Se va a ejecutar hasta que queden listas de un solo tamaño, 
        #izquierda y derecha son listas que sirven como input en mezcla
        mezcla(izquierda)
        mezcla(derecha)

        # Iteradores para recorrer las dos sublistas 
        i = 0
        j = 0

        # Iterador para la lista principal
        k = 0

        # Mientras pueda comparar, porque i o j serán menores al tamaño de la lista, me ayuda a determinar cual es el valor menor y mayor
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            # Para que no vaya al infinito
            k += 1 

        # Sabiendo cual es el menor y mayor, ponga lo que ya ordeno en una nueva lista, para repetir el loop 
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda: {izquierda}, derecha: {derecha}')
        print(lista)
        print(' ')
    return lista


if __name__ == '__main__':
    tamaño = int(input('De que tamaño quieres que sea la lista? '))

    lista = [random.randint(0,100) for x in range(tamaño)]
    print('lista sin ordenar')
    print(lista)
    print(' ')

    ordenada = mezcla(lista)
    print('lista ordenada con mezcla')
    print(ordenada)


