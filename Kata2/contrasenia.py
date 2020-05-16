"""
Escribir un programa que almacene la variable contrasenia y le pida al usuario su password 
y si coincide con la contrasenia, (sin tener en cuenta las mayusculas y minusculas), imprime
correcto sino incorrecto
"""
print("Programa de passwords")
contrasenia = "345treYhJ"
pass_usuario = input("introduzca su pass: ")

if contrasenia==pass_usuario:
    print("Correcto!")
else:
    print("Muy mal!")
