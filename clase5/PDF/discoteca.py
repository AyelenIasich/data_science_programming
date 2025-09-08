'''
Control de acceso a una discoteca

Una discoteca permite el ingreso solo a personas mayores de 18
años. Además, si tienen entre 18 y 21 años, no pueden consumir
alcohol. Pedí al usuario su edad y determiná si puede ingresar y
si puede o no consumir alcohol.

'''

edadUser = int(input("Ingrese su edad: "))
if edadUser >= 18:
    print("Puede ingresar a la discoteca.")
    if edadUser <= 21:
        print("Recorda!! No puede consumir alcohol.")
    else:
        print("Puede consumir alcohol.")
else:
    print("No puede ingresar a la discoteca.")