'''
Hacé una función que se llame ordenar_cadena, que reciba
una palabra como texto y devuelva esa misma palabra con las
letras ordenadas alfabéticamente (respetando mayúsculas y
minúsculas).
-> Probá con esta palabra: "PythonEsDivertido".
'''

def ordenar_cadena(cadena):
    """
    Ordena las letras de una cadena alfabéticamente, respetando mayúsculas y minúsculas.

    Args:
        cadena (str): La cadena a ordenar.

    Returns:
        str: La cadena ordenada alfabéticamente.
    """
    return ''.join(sorted(cadena))

resultado = ordenar_cadena("PythonEsDivertido") 

print(f"resultado: {resultado}")