'''
Calification Student
Según la nota del examen (de 0 a 100), asigná una letra:
A: 90 o más
B: entre 80 y 89
C: entre 70 y 79
D: entre 60 y 69
F: menos de 60

USANDO UNA LISTA DE DICCIONARIOS
'''

calificationCategories = [
    {"letter": "A", "min": 90},
    {"letter": "B", "min": 80},
    {"letter": "C", "min": 70},
    {"letter": "D", "min": 60},
    {"letter": "F", "min": 0} 
]

print("Bienvenido al programa de calificacion de estudiantes")
print("Este programa le ayudara a determinar la calificacion de su examen")

calificationNumber = float(input("Ingrese la calificacion que obtuvo en el examen: "))

def get_calification_letter(calificationNumber):
    for category in calificationCategories:
        if calificationNumber >= category["min"]:
            return category["letter"]
    return None

letterUser = get_calification_letter(calificationNumber)

print(f'A la calificacion {calificationNumber} le corresponde la letra {letterUser}')
print("Fin del programa")
