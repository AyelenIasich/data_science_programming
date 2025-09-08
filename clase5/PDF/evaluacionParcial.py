
'''
Evaluación de un parcial

Un parcial se aprueba con nota 6 o más. Si la nota es menor, se
desaprueba. Si la nota es mayor a 8, se considera destacada.
Pedí al usuario su nota y mostrale el resultado con un mensaje
personalizado.
'''

calificationUser = int(input("Ingrese su nota:"))

if calificationUser < 0 :
    print("La nota no puede ser negativa")
elif calificationUser > 10:
    print("La nota no puede ser mayor a 10")
elif calificationUser >= 6:
    print("Aprobado")
    if calificationUser > 8:
        print("Destacado")  
else:
    print("Desaprobado")