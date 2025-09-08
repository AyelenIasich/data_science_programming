'''
Combinación de ciclos
Crea un programa que imprima la tabla de multiplicar del 1 al 10.
Usa un ciclo for para los números del 1 al 10 y un ciclo while para calcular y mostrar los
productos.
'''


for i in range(1, 11):
    print(f"Tabla del {i}:")
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print()  # Espacio entre tablas