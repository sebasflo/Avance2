import random

list = ("piedra","papel","tijera")

COMPUTADORA = random.choice(list)
JUGADOR = None

while JUGADOR not in list:
    JUGADOR = input('piedra, papel o tijera? :').lower()
