'''
Sumar pares y saltear impares (for + continue)

Sumá todos los números del 1 al 20 que sean pares.
Si el número es impar, usá continue para no sumarlo.
¿Cómo saber si el resultado es correcto?
'''

suma = 0 

for numero in range(1,21):
    if numero % 2 == 0:
        suma += numero 
    else: 
        continue 
    
print(f"La suma de los números pares del 1 al 20 es: {suma}")