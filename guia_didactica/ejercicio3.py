# Suma de números hasta alcanzar un límite
"""
Solicita al usuario números hasta que la suma de ellos supere 100.
Procedimiento paso a paso:
1. Inicializa una variable suma en 0.
2. Usa un bucle si para pedir al usuario que ingrese un número.
3. Suma el número ingresado a la variable suma.
4. Repite mientras la suma sea menor o igual a 100.
5. Al finalizar, muestra la suma total.
"""

total = 0
for i in range(1000):
    print(f"Ingrese un número para sumar a {total}:")
    num = int(input())
    total += num

    if total >= 100:
        print("Has superado el límite de suma [100]")
        print(f"Tu suma total es: {total}")
        break