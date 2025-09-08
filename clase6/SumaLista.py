'''
Creá una función llamada sumar_lista que reciba una lista de
números y devuelva la suma de todos sus elementos.
-> Probá usarla con esta lista: [3, 7, 1, 10].
'''


def sumar_lista(lista):
    '''
    Suma todos los elementos de una lista de números.
    :param lista: Lista de números
    :return: Suma de los elementos de la lista
    '''
    
    return sum(lista)


resultadoSuma = sumar_lista([2,7,1,5])

print(f"La suma de la lista es: {resultadoSuma}")