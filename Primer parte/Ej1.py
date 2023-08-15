""""Suma de números
El siguiente ejemplo solicita al usuario ingresar 2 números y muestra la suma:

n1 = int(input())
n2 = int(input())
suma = n1 + n2
print(suma)
Mofique el programa para que:
Permita ingresar y sumar 3 números en lugar de 2.
Muestre el resultado con un mensaje más amigable para el usuario, por ejemplo: La suma de los números ingresados es 7."""

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
suma = n1 + n2 + n3
print(f"La suma de los numeros es {suma}")