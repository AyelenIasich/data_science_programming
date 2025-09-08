'''
 Adivinar con intentos limitados (while + contador + break)
 
El usuario tiene 3 intentos para adivinar un número secreto.
Si adivina, gana. Si se le acaban los intentos, pierde.
¿Cómo contar los intentos y cortar el bucle correctamente?
'''

intentos = 0 

numero_secreto = 7

while intentos < 3:
    userNumber = int(input("Adivina el número (entre 1 y 10): "))
    if userNumber == numero_secreto:
        print("¡Ganaste!")
        break
    else:
         intentos += 1 
    
if intentos == 3:
    print("Perdiste. El número era", numero_secreto)