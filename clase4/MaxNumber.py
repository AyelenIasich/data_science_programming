'''
El mayor de tres números

Crea un programa que solicite al usuario ingresar tres números 
y determine cuál es el mayor de los tres, 
luego informa al usuario con un mensaje cual es el número mayor.
'''

print("El mayor de tres números")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3
    
print(f"El número mayor es: {mayor}")
print("Fin del programa")