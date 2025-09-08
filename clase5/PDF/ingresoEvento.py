'''
Control de ingreso a un evento

En un evento, se permite la entrada gratuita si el invitado
aparece en una lista VIP. Si no está, debe pagar entrada. Pedí el
nombre del usuario y verificá si está en una lista de 3 nombres
predefinidos.
'''

# clienteVips = ["juan", "pedro", "maria"]

# nombreInvitado = str(input("Cual es su nombre?: ")).strip().lower()

# encontrado = False

# for clienteVip in clienteVips:
#     if nombreInvitado == clienteVip:
#         print("Bienvenido VIP, no debe pagar entrada")
#         encontrado = True
#         break

# if not encontrado:
#     print("No está en la lista VIP, debe pagar entrada")
    

clienteVips = ["juan", "pedro", "maria"]

nombreInvitado = input("¿Cuál es su nombre?: ").strip().lower()

if nombreInvitado in clienteVips:
    print("Bienvenido VIP, no debe pagar entrada")
else:
    print("No está en la lista VIP, debe pagar entrada")
