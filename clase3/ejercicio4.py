'''
Precio total de productos
pedi al usuario el precio de 3 productos y mostra el total a pagar
'''

producto1 = float(input("Ingrese el precio del producto 1: "))
producto2 = float(input("Ingrese el precio del producto 2: "))
producto3 = float(input("Ingrese el precio del producto 3: "))

totalPagar = producto1 + producto2 + producto3  

print(f"El total a pagar es: {totalPagar}")