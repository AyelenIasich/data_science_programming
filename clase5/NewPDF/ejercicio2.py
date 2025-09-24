# numero primo se puede dividir entre 1 y si mismo
# detectar si un numero es primo

user_number = int(input("Ingrese un numero: "))

es_primo = True

if user_number < 2:
    es_primo = False
else:
    for i in range(2, user_number):
        if user_number % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El numero {user_number} es primo")
else:
    print(f"El numero {user_number} no es primo")
