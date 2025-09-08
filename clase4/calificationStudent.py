'''
Calification Student
Según la nota del examen (de 0 a 100), asigná una letra:
A: 90 o más
B: entre 80 y 89
C: entre 70 y 79
D: entre 60 y 69
F: menos de 60
'''
print("Bienvenido al programa de calificacion de estudiantes")
print("Este programa le ayudara a determinar la calificacion de su examen")
calificationNumber = float(input("Ingrese la calificacion que obtuvo en el examen: "))

if calificationNumber >= 90:
    print("Su calificacion es A")
elif calificationNumber >= 80:
    print("Su calificacion es B")
elif calificationNumber >= 70:
    print("Su calificacion es C")       
elif calificationNumber >= 60:
    print("Su calificacion es D")
elif calificationNumber < 60:
    print("Su calificacion es F")

print(f'A la calificacion {calificationNumber} le corresponde la letra {calificationNumber}')
print("Fin del programa")