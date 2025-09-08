'''
Control de velocidad

Un sistema de tránsito detecta la velocidad de los autos. Si un
auto va a más de 80 km/h, se le aplica una multa. Si supera los
100 km/h, se considera una infracción grave. Pedí la velocidad e
informá el tipo de sanción correspondiente.

'''

velocidad  = int(input("Ingrese la velocidad del auto: "))

if velocidad <= 0:
    print("La velocidad no puede ser menor o igual a 0.")
elif velocidad <= 80:
    print("El auto va a una velocidad permitida. No aplica multa.")
elif  80 < velocidad <= 100:
    print("El auto va a una velocidad excesiva. Se le aplicará una multa.")
else:
    print("El auto va a una velocidad excesiva. Se considera una infracción grave.")
