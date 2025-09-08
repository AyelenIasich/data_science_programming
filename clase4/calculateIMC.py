def clasificar_imc(imc):
    categorias = [
        {"maximo": 18.5, "mensaje": "Bajo peso"},
        {"maximo": 24.9, "mensaje": "Peso normal"},
        {"maximo": 29.9, "mensaje": "Sobrepeso"},
        {"maximo": 34.9, "mensaje": "Obesidad grado 1"},
        {"maximo": 39.9, "mensaje": "Obesidad grado 2"},
    ]
    
    for categoria in categorias:
        if imc < categoria["maximo"]:
            return categoria["mensaje"]
    return "Obesidad grado 3 (obesidad mórbida)"

imc_usuario = float(input("Ingrese su IMC: "))
resultado = clasificar_imc(imc_usuario)
print(resultado)
print("Fin del programa")