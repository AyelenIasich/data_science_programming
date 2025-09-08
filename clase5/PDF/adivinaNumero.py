'''
Adiviná el número (while + break)

El programa genera un número secreto entre 1 y 10. El usuario tiene intentos
ilimitados para adivinarlo.
Si acierta, el programa muestra un mensaje y termina con break.
Si no, vuelve a pedir.

¿Cómo evitar que el programa nunca termine si el usuario se equivoca
siempre?

'''
import random

numeroSecreto = random.randint(1, 10)  # Genera un número secreto entre 1 y 10

while True:
    numeroUser = int(input("Adivina el número entre 1 y 10: "))
    if numeroUser == numeroSecreto:
        print("¡Has adivinado el número!")
        break
    else:
        print("No es el número, intenta de nuevo.")