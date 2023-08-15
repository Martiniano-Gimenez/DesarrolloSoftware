"""Bitcoins a Pesos
Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos equivalen 
hoy los Bitcoins (BTC) que encontró guardados en un disco rígido viejo. 
El usuario del programa debe ingresar una cantidad en Bitcoins."""

n = float(input("Ingrese la cantidad de bitcoins: "))

btc_a_pesos = n*8261734

print(f"Sus {n} bitcoins equivalen a {btc_a_pesos} pesos")