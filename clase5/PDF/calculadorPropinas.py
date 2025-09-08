'''
Calculadora de propina

En un restaurante, se recomienda dejar propina según la
experiencia:

● Si fue excelente: 20% del total

● Buena: 15%

● Regular: 10%

● Mala: 0% 

Pedí al usuario cuánto gastó y cómo fue la
atención, luego mostrá el total con propina incluida.
'''

print("Bienvenido a la calculadora de propinas")

montoGastado = float(input("¿Cuánto gastaste?:"))

atencion = str(input("¿Cómo fue la atención? (excelente, buena, regular, mala): ")).strip().lower()

if atencion == "excelente":
    propina = 0.20
elif atencion == "buena":
    propina = 0.15
elif atencion == "regular":
    propina = 0.10
elif atencion == "mala":
    propina = 0.00
else:
    print("Atención no válida. Por favor, ingrese 'excelente', 'buena', 'regular' o 'mala'.")
    exit()
    
propinaAplicada = montoGastado * propina 

totalConPropina = montoGastado + propinaAplicada

print(f"El total a pagar es: ${totalConPropina:.2f} (incluyendo propina de ${propinaAplicada:.2f})")    