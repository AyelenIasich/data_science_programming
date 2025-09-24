# Alternativa 1: Condicionales Anidados
# Clasificación del IMC según la OMS

imc = float(input("Ingrese su IMC: "))

if imc < 18.5:
    print("Bajo peso")
    if imc < 16:
        print("Advertencia: Bajo peso severo")
else:
    if imc < 25:
        print("Peso normal")
    else:
        if imc < 30:
            print("Sobrepeso")
        else:
            if imc < 35:
                print("Obesidad grado I")
            else:
                if imc < 40:
                    print("Obesidad grado II")
                else:
                    print("Obesidad grado III (mórbida)")
                    if imc >= 50:
                        print("Advertencia: Obesidad extrema")

