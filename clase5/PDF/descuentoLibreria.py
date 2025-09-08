'''
Descuento en una librería

Una librería ofrece un 10% de descuento a estudiantes y un 5% a
jubilados. El resto de los clientes no tiene descuento. Pedí al
usuario el monto total de la compra y si es estudiante o jubilado.
Mostrá el total a pagar según corresponda.
'''

montoCompra = float(input("Ingrese el monto total de la compra: "))


esEstudiante = input("¿Es estudiante? (s/n): ").strip().lower() == 's'
#devuelve true si el usuario ingresa s

if not esEstudiante:
   esJubilado = input("¿Es jubilado? (s/n): ").lower() == 's'

# calcular el descuento 

if esEstudiante:
    descuento = 0.10 # 10% de descuento para estudiantes
elif esJubilado:
    descuento = 0.05 # 5% de descuento para jubilados
else:
    descuento = 0.0    
    
#monto a pagar
descuentoAplicado = montoCompra * descuento
totalPagar = montoCompra - descuentoAplicado

print(f"El total a pagar es: ${totalPagar:.2f} con un descuento del {descuentoAplicado:.0f} % ")