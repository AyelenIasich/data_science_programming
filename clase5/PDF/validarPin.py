'''
Validación de PIN con 3 intentos (while + break)
El sistema tiene un PIN predefinido. El usuario tiene 3 intentos para ingresarlo.
Si se equivoca 3 veces, se bloquea.
Si lo ingresa correctamente, accede.
¿Cómo manejar los intentos con while y cortar con break?
'''

pin = 1234 

intentos = 0
intentosPermitidos = 3
print("Bienvenido al sistema de validación de PIN")


while intentos < intentosPermitidos:
    pinUser = int(input("Ingrese su PIN: "))
    if pinUser == pin:
        print("Acceso permitido")
        break
    else:        
        print("PIN incorrecto, intente nuevamente")
        intentos += 1
        
if intentos == intentosPermitidos:
    print("Sorry, solo tenias 3 intentos, su cuenta ha sido bloqueado ")
