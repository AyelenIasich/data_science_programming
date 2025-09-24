
# Clasificación del IMC según la OMS
imc = float(input("Ingrese su IMC: "))

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidad grado I")
elif  35 <= imc < 40:
    print("Obesidad grado II")
else:
    print("Obesidad grado III (mórbida)")
    
    
    
    
    
    
imc = float(input("Ingrese su IMC: "))

if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
elif 30 <= imc < 35:
    categoria = "Obesidad grado I"
elif 35 <= imc < 40:
    categoria = "Obesidad grado II"
else:
    categoria = "Obesidad grado III (mórbida)"

print(f"Su clasificación de IMC es: {categoria}")


# def clasificar_imc(imc):
#     categorias = [
#         {"maximo": 18.5, "mensaje": "Bajo peso"},
#         {"maximo": 24.9, "mensaje": "Peso normal"},
#         {"maximo": 29.9, "mensaje": "Sobrepeso"},
#         {"maximo": 34.9, "mensaje": "Obesidad grado 1"},
#         {"maximo": 39.9, "mensaje": "Obesidad grado 2"},
#     ]
    
#     for categoria in categorias:
#         if imc < categoria["maximo"]:
#             return categoria["mensaje"]
#     return "Obesidad grado 3 (obesidad mórbida)"

# imc_usuario = float(input("Ingrese su IMC: "))
# resultado = clasificar_imc(imc_usuario)
# print(resultado)
# print("Fin del programa")


imc = float(input("Ingrese su IMC: "))

if imc < 18.5:
    print("Bajo peso")
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


