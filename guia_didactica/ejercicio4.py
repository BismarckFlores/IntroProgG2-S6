# Contador regresivo
"""
Solicita al usuario un número positivo e imprime un conteo regresivo hasta 0.
Procedimiento paso a paso:
1. Solicita un número entero positivo.
2. Usa un bucle para que comience desde el número ingresado y vaya disminuyendo hasta 0.
3. Muestra cada número en pantalla
"""

def cuentaRegresiva(num):
    if num >= 0:
        for i in range(num, -1, -1):
            print(i, end=" ")

def main():
    num = int(input("Ingrese un numero entero positivo: "))
    cuentaRegresiva(num)

main()