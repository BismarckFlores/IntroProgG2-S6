# Contar números pares hasta un límite
# Solicita un número positivo y muestra todos los números pares desde 0 hasta ese número.

def numerosPares(num):
    print(f"Numeros pares en el rango de 0 a {num}")
    for i in range (1, num + 1):
        if i % 2 == 0:
            print(i, end=", ")

def main():
    num = int(input("Ingrese un numero positivo para ser el limite: "))
    if num <= 0:
        print("Ingrese un numero valido")
    else: numerosPares(num)

main()