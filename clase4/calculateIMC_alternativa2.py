# Alternativa 2: Con Validación de Entrada y Mensajes Detallados
# Clasificación del IMC según la OMS

try:
    imc = float(input("Ingrese su IMC (debe ser un número positivo): "))
    
    # Validación de entrada
    if imc <= 0:
        print("Error: El IMC debe ser un número positivo")
    elif imc > 100:
        print("Error: El IMC parece ser demasiado alto. Verifique los datos")
    else:
        # Clasificación principal
        if imc < 18.5:
            categoria = "Bajo peso"
            mensaje = "Considere consultar con un nutricionista"
        elif imc < 25:
            categoria = "Peso normal"
            mensaje = "¡Excelente! Mantenga sus hábitos saludables"
        elif imc < 30:
            categoria = "Sobrepeso"
            mensaje = "Considere ajustar su dieta y aumentar la actividad física"
        elif imc < 35:
            categoria = "Obesidad grado I"
            mensaje = "Recomendamos consultar con un médico"
        elif imc < 40:
            categoria = "Obesidad grado II"
            mensaje = "Es importante buscar ayuda médica profesional"
        else:
            categoria = "Obesidad grado III (mórbida)"
            mensaje = "Consulta médica urgente recomendada"
        
        print(f"Categoría: {categoria}")
        print(f"Recomendación: {mensaje}")

except ValueError:
    print("Error: Debe ingresar un número válido")

