'''
Creá una función llamada factorial que reciba un número
entero y devuelva su factorial.
Recordá que el factorial de un número es el resultado de
multiplicar ese número por todos los anteriores hasta llegar a 1.
-> Por ejemplo: el factorial de 4 es 4 * 3 * 2 * 1 = 24.
'''

def factorial(numero):
    if numero == 0  or numero == 1:
        return 1 
    else: 
        print(f"El factorial de {numero} es: {numero} * factorial({numero-1})")
        return numero * factorial(numero-1)


resultadoFactorial = factorial(4)
print(f"El factorial de 4 es: {resultadoFactorial}")
        
  