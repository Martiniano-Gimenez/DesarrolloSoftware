"""Club deportivo
Un club deportivo tiene 4 categorías de asociados según la edad:

infantiles (desde 13 a 15 años)
cadetes (a partir de los 15 y hasta 17)
juveniles (desde los 17 hasta los 19)
mayores (de 19 años en adelante)
Escriba un programa que permita al usuario ingresar el nombre y la edad de un socio y
muestre su el nombre de la categoría en la que le corresponde estar."""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad>=13 and edad<15:
    print("Pertenece a la categoria infantiles")

elif edad>=15 and edad<17:
    print("Pertenece a la categoria cadetes")

elif edad>=17 and edad<19:
    print("Pertenece a la categoria juveniles")

elif edad>=19:
    print("Pertenece a la categoria mayores")

else:
    print("No pertenece a ninguna categoria")