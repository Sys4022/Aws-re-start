import random

print("------------------------------------------GENERADOR DE DOGECOIN 🔮🧙‍♂️------------------------------------------------------")

print("Las reglas son simples, pienso un número y tú adivinas, si adivinas te generas una Dogecoin, si pierdes utilizo tu pc para minar💱")

print("----------------------------------------------------------------------------------------------------------------------------")

Enlace="https://www.youtube.com/watch?v=hvL1339luv0&ab_channel=RapidLiquid"##Importa url
number = random.randint(1,5) # Simulará la acción de "pienso en un número"

isGuessRight = False # Variable bool

# Mientras que "esCorrecto" no sea verdad sigo con el juego
while isGuessRight != True:
    guess = int(input("Ingresa el numero que crees que estoy pensando: "))
    
    if guess == number:
        isGuessRight = True
        print("---------")
        print(f"HAZ GANADO UNA DOGE COIN, HAZ CLIC EN EL SIGUENTE ENLACE {Enlace} ")
        print("---------")
    else:
        print("Casi, sigue intentando🤑")
        print("Esa doge coin no se genera sola💰")
        print("a casa platita ")