
# TestBusquedas.py
# Este es un archivo de prueba muy sencillo, debe ser modificado 
# de acuerdo con el enunciado del laboratorio.

from Busquedas import BusquedaLineal

A1 = [1,3,5,6,7,8,9,0]
e = 9

encontrado = BusquedaLineal(A1, e)
if encontrado != None:
	print("Está en la posición: " + str(encontrado)) 
