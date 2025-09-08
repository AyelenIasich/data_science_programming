'''
Ciclo do while (simulado con while)
Simula un ciclo do while en Python para pedir al usuario que ingrese una contraseña y verifica
si es correcta. Debe continuar pidiendo hasta que se ingrese la contraseña correcta
'''

password = 'Monita123'

while True:
    user_password = str(input('Ingrese la contraseña: '))
    if user_password == password:
        print('Contraseña correcta')
        break
    else:
        print('Contraseña incorrecta, intente nuevamente')