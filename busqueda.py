import random

# Algoritmo de busqueda para ver si esta el objeto en una lista

def busqueda(lista, objtivo):
    match = False

    # El loop crece en función de lista -> O(n) es lineal, porque solo hay un loop

    for elemento in lista:
        if elemento == objtivo:
            match = True

            #para no darle una vuelta a toda la lista debo hacerle un break, pensar en el peor escenario

            break

    return match

# Si quiero que este modulo se pueda importar y ejecutar de manera directa

if __name__ == '__main__':
    tamaño_lista = int(input('De que tamaño será la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]

    encontrado = busqueda(lista, objetivo)
    print(lista)
    print(f'El elemento objetivo es {objetivo} {"esta " if encontrado else "no esta"} en la lista')