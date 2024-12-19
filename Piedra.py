import random

list = ("piedra","papel","tijera")
#buckle
while True:
    COMPUTADORA = random.choice(list)
    JUGADOR = None
#buckle
    while JUGADOR not in list:
        JUGADOR = input('piedra, papel o tijera? :').lower()
#condiciones 
    if JUGADOR == COMPUTADORA :
     print("JUGADOR", JUGADOR)
     print("COMPUTADORA" , COMPUTADORA)
     print("EMPATE!")
    elif JUGADOR == "piedra" :
     if COMPUTADORA == "papel" :
      print("JUGADOR", JUGADOR)
     print("COMPUTADORA" , COMPUTADORA)
     print("PERDISTE!")
     if COMPUTADORA == "tijera" :
         print("JUGADOR", JUGADOR)
         print("COMPUTADORA" , COMPUTADORA)
         print("GANASTE!")
    elif JUGADOR == "papel" :
     if COMPUTADORA == "piedra" :
         print("JUGADOR", JUGADOR)
         print("COMPUTADORA" , COMPUTADORA)
         print("GANASTE!")
     if COMPUTADORA == "tijera" :
         print("JUGADOR", JUGADOR)
         print("COMPUTADORA" , COMPUTADORA)
         print("PERDISTE!")     
    elif JUGADOR == "tijera" :
     if COMPUTADORA == "piedra" :
         print("JUGADOR", JUGADOR)
         print("COMPUTADORA" , COMPUTADORA)
         print("PERDISTE!")
     if COMPUTADORA == "papel" :
         print("JUGADOR", JUGADOR)
         print("COMPUTADORA" , COMPUTADORA)
         print("GANASTE!") 
    Jugar_de_nuevo = input("QUIERES JUGAR DE NUEVO (SI,NO): ").lower()
    if Jugar_de_nuevo != "si" :
        break

print("ADIOS")



     