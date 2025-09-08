
# Operadores relacionales: Crea un programa que compare dos números y determine si el primero es mayor que el segundo 

# print("Bienvenido a la maquina de comparacion de dos numeros")
# num1 = int(input("Ingrese el primer numero "))
# num2 = int(input("Ingrese el segundo numero "))

# if num1 > num2: 
#     print(f"El primer numero '{num1}' es mayor que el segundo '{num2}'")
# elif num1 == num2:
#     print(f"Upps! ambos numero son iguales")
# else:
#     print(f"El segundo numero '{num2}' es mayor que el primero '{num1}'")
    
# print("Fin del programa. Gracias por usar la maquina de comparacion de dos numeros")


#  Operadores lógicos: Construye un programa que determine si un número ingresado por el usuario es par y positivo al mismo tiempo 

# print("Bienvenido a la maquina de verificacion de si un numero es par y positivo al mismo tiempo")

# user_number = input("Ingrese un numero ")

# try:
#     num = int(user_number)
    
#     is_par = num % 2 == 0 
#     is_positivo = num > 0
    
#     if is_par and is_positivo:
#         print(f"El número '{num}' es par y positivo.") 
#     elif not is_par and is_positivo:
#         print(f"El número '{num}' no es par, pero sí es positivo.")
#     elif is_par and not is_positivo:
#         print(f"El número '{num}' es par, pero no es positivo.")
#     else:
#         print(f"El número '{num}' no es par ni positivo.")
    
# except ValueError:
#     print(f"El numero '{user_number}' no es un numero entero")
    
# print("Fin del programa. Gracias por usar la máquina de verificación.")


#  Conversión de tipos: Realiza una concatenación de una cadena y un número, convirtiendo el número a cadena.

# print("Bienvenido a la conversion de tipos")

# cadena = "Hola"
# numero = 123

# print(f"Esto es la concatenacion de una cadena y un numero: {cadena} {str(numero)}")
# print("Esto es una cadena" + str(numero))


# Expresiones condicionales: Crea un programa que determine si un año ingresado por el usuario es un año bisiesto o no, usando expresiones lógicas

# print("Bienvenido a la verificacion de si un año es bisiesto o no")

# year_user = int(input("Ingrese un año: "))

# is_bisiesto = ((year_user % 4 == 0 and year_user % 100 != 0) or (year_user % 400 == 0))

# if is_bisiesto:
#     print(f"El año '{year_user}' es bisiesto")
# else:
#     print(f"El año '{year_user}' no es bisiesto")
    
# print("Fin del programa. Gracias por usar la verificacion de si un año es bisiesto o no")


#  Expresiones complejas: Escribe un programa que determine si un número es divisible por 3 y 5 al mismo tiempo

print("Bienvenido a la verificacion de si un numero es divisible por 3 y 5 al mismo tiempo")

user_number = int(input("Ingrese un numero: ")) 

is_divisible_by_3 = user_number % 3 == 0
is_divisible_by_5 = user_number % 5 == 0


if is_divisible_by_3 and is_divisible_by_5:
    print(f"El numero '{user_number}' es divisible por 3 y 5 al mismo tiempo")
else:
    print(f"El numero '{user_number}' no es divisible por 3 y 5 al mismo tiempo")
    
print("Fin del programa. Gracias por usar la verificacion de si un numero es divisible por 3 y 5 al mismo tiempo")


