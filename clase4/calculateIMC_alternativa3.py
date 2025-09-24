# Alternativa 3: Con Cálculo Automático del IMC
# Clasificación del IMC según la OMS

print("=== Calculadora de IMC ===")
print("Opción 1: Ingresar IMC directamente")
print("Opción 2: Calcular IMC con peso y altura")

opcion = input("Seleccione una opción (1 o 2): ")

if opcion == "1":
    # Opción original - ingresar IMC directamente
    imc = float(input("Ingrese su IMC: "))
    
elif opcion == "2":
    # Nueva opción - calcular IMC
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Error: Peso y altura deben ser números positivos")
        else:
            imc = peso / (altura ** 2)
            print(f"Su IMC calculado es: {imc:.2f}")
    
    except ValueError:
        print("Error: Debe ingresar números válidos")
        imc = 0  # Valor por defecto para evitar errores
        
else:
    print("Opción no válida")
    imc = 0

# Clasificación (solo si se ingresó un IMC válido)
if imc > 0:
    print("\n=== Clasificación ===")
    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    elif 30 <= imc < 35:
        print("Obesidad grado I")
    elif 35 <= imc < 40:
        print("Obesidad grado II")
    else:
        print("Obesidad grado III (mórbida)")

