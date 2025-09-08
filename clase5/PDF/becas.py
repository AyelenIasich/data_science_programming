'''
Sistema de becas

Para obtener una beca, un estudiante debe cumplir al menos
una de estas condiciones:

● Tener un promedio mayor a 8

● O bien, tener promedio mayor a 6 y bajos recursos 
Pedí al usuario su promedio y si tiene bajos recursos. Informá si
accede a la beca o no.
'''

print("Bienvenido al sistema de becas")
promedio = float(input("Ingrese su promedio: "))
is_bajos_recursos = input("Tiene bajos recursos?(s/n):").strip().lower() == "s"

if promedio > 8:
    print("Felicitaciones! Accede a la beca.")
elif promedio > 6 and is_bajos_recursos:
    print("Felicitaciones! Accede a la beca.")
else:
    print("Lo sentimos, no accede a la beca.")