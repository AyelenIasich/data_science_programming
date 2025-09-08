'''
Validación de menú (while + break)

Mostrá un menú simple:
1. Jugar
2. Ver puntuación
3. Salir

El usuario debe ingresar una opción válida (1, 2 o 3).
Si elige 3, el programa finaliza.

Si ingresa otra opción, debe volver a preguntar.
¿Cómo controlar el bucle con while y terminar con break?
'''

while True:
    print("1. Jugar")
    print("2. Ver puntuación")
    print("3. Salir")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    if opcion == "1":
        print("Iniciando juego...")
    elif opcion == "2":
        print("Mostrando puntuación...")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")