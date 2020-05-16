"""
Problema de panaderia
"""
precio = 3.49
descuento = 1 -0.6
precio_con_descuento = precio * descuento
numero_de_barras = input("Introduce el numero de barras vendidas:")
numero_de_barras = int(numero_de_barras)
print("Precio habitual: "+str(precio))
print("Precio con descuento: "+str(precio_con_descuento))
print("Coste final: "+str(precio_con_descuento*numero_de_barras))