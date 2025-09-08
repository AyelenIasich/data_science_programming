'''
Clasificación de peso para boxeo

En una competencia de boxeo, los luchadores se clasifican
según su peso:

● Menos de 60 kg: "Peso ligero"

● Entre 60 y 80 kg: "Peso medio"

● Más de 80 kg: "Peso pesado" Pedí al usuario su peso y
mostrá su categoría.

'''

pesoBoxeador = float(input("Ingrese su peso en kg: "))

# Validar que el peso sea un número positivo
if pesoBoxeador <= 0:
    print("El peso debe ser un número positivo, por favor intente de nuevo.")
    pesoBoxeador = float(input("Ingrese su peso en kg: "))

if pesoBoxeador < 60:
    categoria = "Peso ligero"
elif 60 <= pesoBoxeador <= 80:
    categoria = "Peso medio"
else:
    categoria = "Peso pesado"
    
print(f"Su categoría es: {categoria}")