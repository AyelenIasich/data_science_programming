'''
Calcular el área de un rectangulo a partir de su base y altura.
Pedirle al usuario la base y la altura del rectangulo y calcular el área y mostrarla por pantalla.
area = (base * altura)
'''

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = base * altura

print(f"El area del rectangulo de base {base} y altura {altura} es: {area}")