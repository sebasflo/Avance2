import random

list = ("piedra","papel","tijera")

COMPUTADORA = random.choice(list)
JUGADOR = None

while JUGADOR not in list:
    JUGADOR = input('piedra, papel o tijera? :').lower()

if JUGADOR == COMPUTADORA :
     print("COMPUTADORA", COMPUTADORA)
     print("JUGADOR" , JUGADOR)
     print("EMPATE!")
elif JUGADOR == "piedra" :
    if COMPUTADORA == "papel" :
     print("COMPUTADORA", COMPUTADORA)
     print("JUGADOR" , JUGADOR)
     print("PERDISTE!")
    if COMPUTADORA == "tijera" :
     print("COMPUTADORA", COMPUTADORA)
     print("JUGADOR" , JUGADOR)
     print("GANASTE!")
     