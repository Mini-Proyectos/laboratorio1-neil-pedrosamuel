import sys
import insertsort

Array = []

name = sys.argv[1]

archivo = open(name,'r+')

while True:
	linea = archivo.readline()
	if not linea:
		break
	Array.append(int(linea))

archivo.close()

insertsort.insertSort(Array)

