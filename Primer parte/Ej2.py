"""Promedio de temperaturas
Durante los 5 días de una semana se tomaron mediciones de temperatura en la ciudad. 
Se desea conocer cuál fue la temperatura promedio de la semana. 
Escriba un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario."""

t1 = float(input("Ingrese la temperatura del dia 1: "))
t2 = float(input("Ingrese la temperatura del dia 2: "))
t3 = float(input("Ingrese la temperatura del dia 3: "))
t4 = float(input("Ingrese la temperatura del dia 4: "))
t5 = float(input("Ingrese la temperatura del dia 5: "))

suma_temp = t1 + t2 + t3 + t4 + t5
promedio_temp = suma_temp/5

print(f"El promedio de las temperaturas es: {promedio_temp}")