'''

Calculas precio final del envío

Una empresa de transporte ofrece su servicio para enviar paquetes a tres provincias de la Patagonia Argentina. 

Cuando un cliente quiere enviar un paquete, puede elegir por distintos tipos de pesos 
Ej: (paquete de 15 kg a 20 kg). 

El cliente contrata el servicio de transporte eligiendo una provincia como destino y un peso de paquete. 

Se necesita realizar un algoritmo para saber el precio final a pagar. 

En la siguiente tabla se muestran los destinos con cada peso admitido y su precio correspondiente.
'''


print("Bienvenido al sistema de envío de paquetes a la Patagonia Argentina")
print("Por favor, elija una provincia de destino y el peso del paquete para calcular el precio final del envío.")
pesoPaquete = float(input("Ingrese el peso del paquete (kg) - Solo aceptamos paquetes de 15kg a 20kg: "))
provinciaDestino = str(input("Ingrese la provincia de destino (Santa Cruz, Chubut, Rio Negro): "))

provinciaDestino = provinciaDestino.strip()

if provinciaDestino == "":
    print("Debe ingresar una provincia válida.")
    exit()

provinciaDestino = provinciaDestino.lower()

if provinciaDestino == "santa cruz":
    if pesoPaquete >= 11 and pesoPaquete <=20:
        print(f"Debe abonar $400 pesos, por el paquete de {pesoPaquete} kilos") 
    elif pesoPaquete >= 6 and pesoPaquete <= 10:
       print(f"Debe abonar $300 pesos, por el paquete de {pesoPaquete} kilos") 
    elif pesoPaquete > 0  and pesoPaquete <= 5:
        print(f"Debe abonar $200 pesos, por el paquete de {pesoPaquete} kilos") 
    else:
        print("Peso no admitido para el envío a Santa Cruz")
elif provinciaDestino == "chubut":    
    if pesoPaquete >= 16 and pesoPaquete <=25:
        print(f"Debe abonar $420 pesos, por el paquete de {pesoPaquete} kilos") 
    elif pesoPaquete >= 11 and pesoPaquete <= 15:
       print(f"Debe abonar $390 pesos, por el paquete de {pesoPaquete} kilos") 
    elif pesoPaquete > 0  and pesoPaquete <= 10:
        print(f"Debe abonar $350 pesos, por el paquete de {pesoPaquete} kilos") 
    else:
        print("Peso no admitido para el envío a Chubut")
elif provinciaDestino == "rio negro":
    if pesoPaquete >= 19 and pesoPaquete <=26:
        print(f"Debe abonar $420 pesos, por el paquete de {pesoPaquete} kilos") 
    elif pesoPaquete >= 13 and pesoPaquete <= 18:
       print(f"Debe abonar $390 pesos, por el paquete de {pesoPaquete} kilos") 
    elif pesoPaquete > 0  and pesoPaquete <= 12:
        print(f"Debe abonar $400 pesos, por el paquete de {pesoPaquete} kilos") 
    else:
        print("Peso no admitido para el envío a Rio Negro")
else:    
    print("No realizamos envios a esa provincia")
    
print("Gracias por usar nuestro servicio de envíos a la Patagonia Argentina.")
    