'''
Creá un diccionario en Python que almacene nombres de personas como claves y sus edades como valores. 
Luego, agregá una persona nueva al diccionario y mostrá todas las claves y valores con un bucle
'''

# Crear un diccionario con nombres y edades
personas = {
    "Juan": 25,
    "María": 32,
    "Carlos": 45,
    "Laura": 29
}

# Agregar una persona nueva al diccionario
personas["Ana"] = 38

# Mostrar todas las claves y valores con un bucle
print("Lista de personas y edades:")
for nombre, edad in personas.items():
    print(f"{nombre}: {edad} años")
    
    
# Usando una lista de tuplas (nombre, edad)
personas = [("Juan", 25), ("María", 32), ("Carlos", 45), ("Laura", 29)]

# Agrego una persona nueva
personas.append(("Ana", 38))

# Muestro todas las personas y edades
print("Lista de personas y edades:")
for nombre, edad in personas:
    print(f"{nombre}: {edad} años")
    
    