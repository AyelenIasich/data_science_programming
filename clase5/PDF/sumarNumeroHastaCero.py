'''
Sumar números hasta cero (while)

El usuario va ingresando números uno por uno. Cuando ingresa 0, el programa
se detiene y muestra la suma total.
¿Qué pasaría si el cero se pone al principio? ¿Y si nunca se pone?

'''


sumaTotal = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    if numero == 0: 
        break
    sumaTotal += numero
    
print("La suma total es:", sumaTotal)