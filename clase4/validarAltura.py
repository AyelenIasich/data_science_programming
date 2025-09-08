'''
Validar altura de una persona

Realizar un programa calcule si una persona es de estatura baja, media o alta.
En tales casos, informar…

Si la altura es menor o igual a 150 cm →  “Persona de altura baja”;  

Si la altura está entre 151 y 170 →  “Persona de altura media”

Si la altura es mayor al 171 →  “Persona alta”.
'''

print("Bienvenido al programa de validacion de altura") 
print("Este programa le ayudara a determinar la altura de una persona")

alturaUser = float(input("Ingrese la altura de la persona en cm: "))
if alturaUser >= 170:
    print("Persona de altura alta")
elif alturaUser >= 151:
    print("Persona de altura media")
elif alturaUser <= 150:
    print("Persona de altura baja")
else:
    print("Altura no valida")
print("Gracias por usar el programa de validacion de altura") 