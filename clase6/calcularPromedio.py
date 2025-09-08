
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        numeros (list): Lista de números (int o float).

    Retorna:
        float: El promedio de los números en la lista.
               Si la lista está vacía, retorna None.
    """
    if not numeros:
        return None
    return sum(numeros) / len(numeros)


listaNumeros = [7, 5, 8, 9, 9, 6]

if len(listaNumeros) == 0:
    print("La lista está vacía. Por favor, ingrese números.")
else:
    promedio = sum(listaNumeros) / len(listaNumeros)
    print(f"El promedio es: {promedio:.2f}")
