"""
	archivo: problema1.py
	Problema 1 del taller de laboratorio
	autor: @jecueva1997
"""
# Ingreso de datos
horas = input("Ingrese las horas: ") 
costo = input("Ingrese el costo por hora trabajada: ") 
# Se calcula el sueldo total
sueldo1 = float(horas) * float(costo) 
# Se calcula el descuento
seguro = float(sueldo1) * 0.10 
# Se calcula el sueldo mensual
sueldo1 = float(sueldo1) - float(seguro) 
# Se presentan los datos
print ("El costo del seguro es: %.2f\nEl sueldo es: %.2f" % (seguro, sueldo1))