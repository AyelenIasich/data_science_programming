'''
10. Elección de menú saludable
Un menú saludable ofrece tres opciones:

● A: Ensalada con agua
● B: Sándwich integral con jugo natural
● C: Comida rápida con gaseosa (no recomendado) 

Pedí al usuario que elija una opción. Si elige la opción C, mostrá
una advertencia sobre alimentación saludable.
'''

print("Menú saludable:")
print("A: Ensalada con agua")
print("B: Sándwich integral con jugo natural")
print("C: Comida rápida con gaseosa (no recomendado)")

opcion = input("Elija una opción (A, B o C): ").strip().upper()

if opcion == "A":
    print("Has elegido Ensalada con agua. ¡Buena elección!")
elif opcion == "B": 
    print("Has elegido Sándwich integral con jugo natural. ¡Buena elección!")
elif opcion == "C":
    print("Has elegido Comida rápida con gaseosa. No recomendado para una alimentación saludable.")
else:  
    print("Opción no válida. Por favor, elige A, B o C.")