# print("Programa para ingreso a ver pelicula segun edad ")

# edad_usuario = int(input("Ingrese su edad: "))

# if edad_usuario >= 13 and edad_usuario <= 100:
#     print("Bienvenido, tienes permitido ver la pelicula")
# elif edad_usuario > 1:
#     print("Lo siento, no tienes permitido ver la pelicula")
# else:
#     print("Edad no valida, por favor ingrese una edad correcta")

# ====================================================================================

# print("Bienvenido profesor al programa de calificacion de estudiantes")
# print("Este programa le ayudara a determinar la calificacion de los examenes de tus estudiantes")

# calificationNumber = int(input("Ingrese la calificacion que obtuvo el estudiante en el examen: "))
# calificationLetter = ""

# if calificationNumber >= 90:
#     calificationLetter = "A"
# elif calificationNumber >= 80:
#     calificationLetter = "B"
# elif calificationNumber >= 70:
#     calificationLetter = "C"
# elif calificationNumber >= 60:
#     calificationLetter = "D"
# else:
#     calificationLetter = "F"


# print(f'A la calificacion {calificationNumber} le corresponde la letra {calificationLetter}')

# ====================================================================================

# calificationCategories = [
#     {"letter": "A", "min": 90},
#     {"letter": "B", "min": 80},
#     {"letter": "C", "min": 70},
#     {"letter": "D", "min": 60},
#     {"letter": "F", "min": 0}
# ]

# print("Bienvenido profesor al programa de calificacion de estudiantes")
# print("Este programa le ayudara a determinar la calificacion de los examenes de tus estudiantes")

# calificationNumber = int(input("Ingrese la calificacion que obtuvo el estudiante en el examen: "))

# def get_calification_letter(calificationNumber):
#     for category in calificationCategories:
#         if calificationNumber >= category['min']:
#             return category['letter']
#     return None

# letterUser = get_calification_letter(calificationNumber)

# print(f'A la calification {calificationNumber} le corresponde la letra {letterUser}')
# print("Fin del programa")


# ====================================================================================

# print("Bienvenido al programa calculador de descuentos")

# priceProduct = float(input("ingrese el precio del producto: "))
# priceFinal = 0
# descuent = 0

# if priceProduct >= 12999:
#     descuent = priceProduct * 0.3
# else:
#     descuent = priceProduct * 0.2

# priceFinal = priceProduct - descuent

# print(f"El precio final del producto es: {priceFinal}")

# ====================================================================================