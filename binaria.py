import random

'''
    import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
'''

def busqueda(lista, comienzo, final, objtivo):

    print(f'Estoy buscando el numero {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

    # Termino la busqueda porque no esta el objetivo

    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    # Ya lo encontre

    if lista[medio] == objetivo:
        return True
    
    # No lo he encontrado y hago la division, comienzo = medio + 1 cuando me voy a la parte de arriba

    elif lista[medio] < objetivo:
        return busqueda(lista, medio + 1, final, objtivo)
    else:
        return busqueda(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    tamaño_lista = int(input('De que tamaño será la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamaño_lista)])

    encontrado = busqueda(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento objetivo es {objetivo} {"esta " if encontrado else "no esta"} en la lista')


    '''
  if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    '''