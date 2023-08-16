# -*- coding: utf-8 -*-
import db_productos
from db_productos import cargar_productos

productos = []
#1b: cargar la lista de productos con la función
productos = cargar_productos()

#2: definir una función mostrar_productos()
#          que reciba la lista de productos, no retorne nada,
#          y muestre la lista utilizando el siguiente formato para cada producto:
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# ...
def mostrar_productos(productos):
    for i in productos:
        print(f"Producto {i['id']}")
        print(f"{i['nombre']} ${i['precio']}")
        print("------------------------------------------------")


def calcular_precio_actualizado(porcentaje_aumento,precio_sin_aumento):
    porcentaje_con_aumento = porcentaje_aumento/100
    precio_con_aumento = precio_sin_aumento + (precio_sin_aumento * porcentaje_con_aumento)
    return precio_con_aumento

        
# TODO #3: definir una función calcular_precio_actualizado()
#          que reciba: el precio anterior y porcentaje de aumento
#          y retorne: el precio con el aumento.


def actualizar_precios(productos,porcentaje_aumento):
    for i in productos:
        precio_sin_aumento = i["precio"]
        precio_actualizado = calcular_precio_actualizado(porcentaje_aumento,precio_sin_aumento)
        i["precio"] = precio_actualizado
        
# TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y 
#          el porcentaje de aumento. La función debe recorrer cada producto de la
#          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
#          el precio del producto y el porcentaje de aumento) para obtener el precio
#          actualizado y modifique la lista "in-place" actualizando el precio de cada
#          producto. La función no debe retornar nada sino dejar modificada la lista
#          pasada por el usuario.

if __name__ == '__main__':
    # TODO #5a: mostrar la lista cargada
    mostrar_productos(productos)
    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
    porcentaje_aumento = int(input("Ingrese el porcentaje de aumento: "))
    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
    actualizar_precios(productos,porcentaje_aumento)
    # TODO #5d: mostrar la lista con los precios actualizados
    mostrar_productos(productos)