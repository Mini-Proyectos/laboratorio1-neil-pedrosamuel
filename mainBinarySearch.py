import sys
import binarySearch
import verificarOrden

Array = []

name = sys.argv[1]
x = sys.argv[2]

archivo = open(name,'r+')

while True:
	linea = archivo.readline()
	if not linea:
		break
	Array.append(int(linea))

archivo.close()

if(verificarOrden.verificarOrden(Array)):
	binarySearch.binarySearch(0,len(Array),int(x),Array)
else:
	print('El arreglo esta desordenado')

