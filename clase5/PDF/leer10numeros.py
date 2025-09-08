'''
Leer 10 números, pero detenerse si uno es negativo (for + break)
Pedí al usuario 10 números.
Si uno es negativo, el programa termina antes de leer todos.
¿Cómo controlar el for con break?

'''

numerosUser = []

for i  in range(10):
    numero = int(input("Ingrese un número: "))
    
    if numero < 0:
        print("Número negativo. Terminando la lectura.")
        break  
    
    numerosUser.append(numero)
    
print("Números ingresados:", numerosUser)