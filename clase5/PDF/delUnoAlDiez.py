'''
Números del 1 al 10, menos el 5 (for + continue)

Usá un bucle for para mostrar los números del 1 al 10, excepto el 5.
Usá continue para saltearlo.
¿Qué pasaría si se usa break en lugar de continue?
No llegariamos nunca a mostrar los números 6, 7, 8, 9 y 10.
'''


for num in range(1,11):
    if num == 5:
        continue
    print(num)  
