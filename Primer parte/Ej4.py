"""Descuento en el supermercado
Un supermercado tiene una promoción especial: 
si una compra supera los $3500 entonces se aplica un descuento del 10% a la venta. 
Por ejemplo, si un cliente realiza una compra por $3000, pagará $3000, pero si realiza 
una compra por $3600, entonces pagará $3240, ya que tendrá un descuento del 10% (en este caso $360) sobre el total. 
Escribir un programa que permita ingresar el monto de la compra e 
informe el importe final que deberá pagar el cliente, con o sin el descuento según corresponda."""

compra = float(input("Ingrese el importe de su compra: "))

if compra>3500:
    compra2 = compra - (compra*0.10)
    print(f"El importe de su compra con descuento es: {compra2}")

else:
    print(f"No obtiene descuento. Su importe es de: {compra}")