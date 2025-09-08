'''
Conversor de pesos a dolares
pedi al usuario que ingrese una cantidad de pesos y el valor del dolar. Mostra cuantos dolares equivalen
'''

cantPesos = float(input("Ingrese la cantidad de pesos: "))  
valorDolar = float(input("Ingrese el valor del dolar: "))

cantDolares = cantPesos / valorDolar

print(f"{cantPesos} pesos equivalen a {cantDolares} dolares")
