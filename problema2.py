"""
	archivo: problema2.py
	Problema 2 del taller de laboratorio
	autor: @jecueva1997
"""
# Ingreso de datos
x = input("Ingrese el valor de la variable x: ")
y = input("Ingrese el valor de la variable y: ")
z = input("Ingrese el valor de la variable z: ")
# Se realiza la operación y se almacena en las variables
m = ((float(x) + float(y) / float(z)) / (float(x) - float(y) / float(z)))
# Se presentan los datos
print("x = %.1f\n\ty = %.1f\n\tz= %.1f\nEl resultado es: \n\t m = %.1f" % (float(x), float(y), float(z), m))
