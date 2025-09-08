'''
Ciclo for
Crea un programa que recorra una lista de frutas y muestre cada fruta en la consola. Usa un
ciclo for.
'''

print("Inicio del bucle for")
listaFruta = ["manzana", "pera", "naranja", "uva", "sandia"]

for i in listaFruta:
    print(f"El valor de i en cada iteracion {i}")

print("Fin del bucle for")

print("=============================================")

'''
Podriamos usar range() si quisiéramos acceder por índice, así:
Acá usamos range() para obtener los índices del 0 al 4, y accedemos a cada fruta con frutas[i].
'''
print("Inicio del bucle for range")

frutas = ["manzana", "banana", "naranja", "uva", "kiwi"]

for i in range(len(frutas)):
    print(frutas[i])
    
print("Fin del bucle for")