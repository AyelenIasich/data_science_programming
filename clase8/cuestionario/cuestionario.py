cubo = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print(f"Cubo[1][0][1] = {cubo[1][0][1]}")

mi_vector = [10, 20, 30, 40]

print(f"mi_vector[2] = {mi_vector[2]}")
# ============================================================

mi_conjunto = {1, 2, 3, 2, 4, 3, 5}

print("Conjunto original:", mi_conjunto)
# Agregamos un elemento nuevo
mi_conjunto.add(6)

# Intentamos agregar un duplicado
mi_conjunto.add(3)

print("Despues de agregar elementos:", mi_conjunto)

lista = [1, 2, 2, 3, 4, 4, 5]
print("Lista original:", lista)
conjunto = set(lista)
print("Conjunto desde una lista con duplicados:", conjunto)

numeros = {1, 2, 2, 3}
print(numeros)

# ============================================================

matriz = [[1, 2], [3, 4]]
print(matriz[1][0])

frutas = ["manzana", "banana"]
frutas.append("pera")
print(frutas)

mi_tupla = (1, 2, 3)
mi_tupla[0] = 99