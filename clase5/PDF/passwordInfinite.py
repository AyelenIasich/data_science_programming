'''
Repetir contraseña hasta que coincida (while)

El sistema pide que se escriba una contraseña, y luego que se repita.
Si las contraseñas no coinciden, vuelve a pedirlas.
¿Cómo usar while para repetir el proceso hasta que ambas contraseñas sean
iguales?
'''

while True:
    passwordUser = str(input('Escribe la contraseña: '))
    passwordUser2 = str(input('Repite la contraseña: '))
    
    if passwordUser == passwordUser2:
        print('Las contraseñas coinciden')
        break
    else:
        print('Las contraseñas no coinciden, vuelve a intentarlo')
        continue

