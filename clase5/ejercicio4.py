'''
Uso de break
Escribe un programa que pida números al usuario hasta que se ingrese un número negativo.
Utiliza break para salir del bucle.
'''

while True:
    numeroUser = int(input("Ingrese un número (negativo para salir): "))
    if numeroUser < 0:
        break
    