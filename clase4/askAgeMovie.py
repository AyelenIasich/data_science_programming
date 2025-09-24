'''
Verifica la edad para ver una pelicula 
Pedile al usuario su edad y permitile ver la pelicula solo si tiene 13 anos o mas.
'''

print("Clasificacion de edad para ver una pelicula")

edadUser = int(input("Cuantos años tienes? "))

if edadUser >= 13:
    print("Bienvenido, tienes permitido ver la pelicula")
else:
    print("Lo siento, no tienes permitido ver la pelicula")
    
    
    
