import random

def generarLista():
    lista = []
    for i in range(0, 10):
        numero = random.randint(1, 20)
        lista.append(numero)
    return lista


def mayor(lista_generada, valor_ingresado):
    cont=0
    for i in lista_generada:
        if i>valor_ingresado:
            cont=cont+1
    return cont

def promedio(lista_generada):
    suma = 0
    for i in lista_generada:
      suma = suma + i
    prom = suma/10
    return prom
    
def mayorYmenor(lista_generada):
    mayor = lista_generada[0]
    menor = lista_generada[0]
    for i in lista_generada:
        if i>mayor:
            mayor = i
        if i<menor:
            menor = i    
    return (mayor, menor)

lista_generada = generarLista()
print(lista_generada)

valor = int(input("Ingrese un valor: "))
contador = mayor(lista_generada, valor)
print(f"La cantidad de valores de la lista que son mayores al valor ingresado es: {contador}")

prom = promedio(lista_generada)
print(f"El promedio de la lista es: {prom}")

(mayor, menor) = mayorYmenor(lista_generada)

print(f"El menor valor es {menor} y el mayor valor es {mayor}")