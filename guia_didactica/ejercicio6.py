# Promedio de calificaciones
"""
Solicita una cantidad indeterminada de calificaciones hasta que el usuario ingrese -1.
Calcula y muestra el promedio.
Procedimiento paso a paso:
1. Inicializa suma y contador en 0.
2. Usa un bucle repetir-hasta para pedir una calificación.
3. Si el número ingresado es diferente de -1, suma la calificación y aumenta el contador.
4. Finaliza cuando el usuario ingresa -1.
5. Calcula y muestra el promedio.
"""

print("Ingrese sus calificaciones. Escriba -1 para finalizar.")

suma = 0
contador = 0

for i in range(1000):  # Se usa un rango grande para permitir muchas entradas
    nota = float(input("Ingrese una calificación (-1 para terminar): "))
    if nota == -1:
        break
    if nota < 0 or nota > 100:
        print("Calificación inválida. Debe estar entre 0 y 100.")
        continue
    suma += nota
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de las {contador} calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")