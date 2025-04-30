# Adivinar un número
"""
Genera un número aleatorio entre 1 y 10. El usuario debe adivinarlo. El programa da
pistas: "mayor" o "menor".
Procedimiento paso a paso:
1. Genera un número aleatorio entre 1 y 10.
2. Solicita al usuario que ingrese un número.
3. Mientras el número ingresado sea diferente al número generado:
− Informa si debe intentar con un número mayor o menor
− Pide un nuevo número
4. Felicita al usuario al adivinarlo.
"""

import random

def numeroAleatorio(num):
    aleatorio = random.randint(1, 10)
    for i in range(100):
        if num == aleatorio:
            print(f"Has adivinado el número")
            break
        elif num > aleatorio:
            print("Es un número menor")
        else:
            print("Es un número mayor")

        num = int(input("Ingrese otro número: "))
    else:
        print("Has superado el limite maximo de intentos")

def main():
    num = int(input("Ingrese un número entre el 1 al 10: "))
    if num >= 1 and num <= 10:
        numeroAleatorio(num)
    else:
        print("Error. Ingrese un número válido")

main()