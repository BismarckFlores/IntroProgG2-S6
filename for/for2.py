# Leer un numero ingresado por el usuario
# mostrar la letra a por cada numero del 1 al numero
# ingresado por el usuario ejemplo, Numero: 3
# a
# aa
# aaa

def mostrarLetra(numero):
    for i in range(1, numero + 1):
        print(f"a" * i)
        
def main():
    num = int(input("Ingresa un número: "))
    mostrarLetra(num)
    
main()