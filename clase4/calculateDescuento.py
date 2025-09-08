'''
Calculadora de descuento
Pedí el precio de un producto y aplica un descuento:
a. Si cuesta $12.999 o más → 30% de descuento
b. Si cuesta menos → 20% de descuento
'''

def calculate_discount(price):
    if price >= 12.999:
        discount = 0.30
    else:
        discount = 0.20
    return price * discount

print("Bienvenido a la calculadora de descuento")
precio = float(input("Ingrese el precio del producto: "))
descuentoObtenido = calculate_discount(precio)
precioFinal = precio - descuentoObtenido
print(f"El descuento aplicado es de: ${descuentoObtenido:.2f}")
print(f"El precio final es de: ${precioFinal:.2f}")
print("Fin del programa")