"""Asado
Franco está organizando un asado con sus amigos y necesita de tu ayuda.
Para estimar cuánta carne necesita comprar, va a suponer que cada invitado come 0.7 Kg de carne. 
Ayuda a Franco escribiendo un programa que permita al usuario ingresar la cantidad de invitados y 
el precio de 1Kg. de carne, y muestre cuántos Kg de carne en total debe pedir al carnicero y 
cuánto dinero necesita para pagar."""

cantInvitados = int(input("Ingrese la cantidad de invitados: "))
precioCarne = float(input("Ingrese el precio de 1kg de carne: "))

kgTotal = 0.7 * cantInvitados

precio = kgTotal * precioCarne

print(f"Deberá comprar {kgTotal}kg de carne")
print(f"Deberá pagar ${precio}")