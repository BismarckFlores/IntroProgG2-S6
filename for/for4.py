# Tabla de multiplicar del numero ingresado

def tablaMultiplicar(num):
    for i in range(1, 13):
        mul = num * i
        print(f"{num} * {i} = {mul}")

def main():
    numero = int(input("Ingrese un numero: "))
    tablaMultiplicar(numero)

main()