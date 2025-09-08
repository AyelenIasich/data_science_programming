'''
Validar dias de la semana

Crea un programa que pida al usuario ingresar un número del 1 al 7 
y muestre el día de la semana correspondiente. 
Si ingresa un número fuera de ese rango, 
mostrar el siguiente mensaje de error: "Número de día incorrecto".
'''

def validateDay(numberDay):
    if numberDay == 1:
        return "Lunes"
    elif numberDay == 2:
        return "Martes"
    elif numberDay == 3:
        return "Miércoles"
    elif numberDay == 4:
        return "Jueves"
    elif numberDay == 5:
        return "Viernes"
    elif numberDay == 6:
        return "Sábado"
    elif numberDay == 7:
        return "Domingo"
    else:
        return "Número de día incorrecto"
    
print("Validemos el dia de la semana")

numberDay = int(input("Ingrese un número del 1 al 7: "))

dayChoosen = validateDay(numberDay)
print(f"El día de la semana correspondiente a tu numero es: {dayChoosen}")
print("Fin del programa")