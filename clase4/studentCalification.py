'''
Notas de un alumno

Crea un programa que determine y muestre al alumno,
según la nota que ingrese, a que categoría pertenece de calificación. 
Si la nota no corresponde con las categorías, mostrar el mensaje "La nota ingresada es invalida".

Las categorías son: 

Suspenso → Notas: 0, 1, 2, 3, 4 y 5 

Aprobado → Nota: 6 

Buena → Nota: 7 

Notable → Nota: 8 

Sobresaliente → Notas: 9 y 10 
'''

calificationStudent = float(input("Ingrese la calificación del alumno: "))    
if calificationStudent >= 9:
    print("Sobresaliente")
elif calificationStudent >= 8: 
    print("Notable")
elif calificationStudent >= 7:
    print("Buena")
elif calificationStudent >= 6:
    print("Aprobado")
elif calificationStudent < 6:
    print("Suspenso")
else: 
    print("La nota ingresada es invalida")
# Fin del programa
    
    