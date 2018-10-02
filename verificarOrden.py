def verificarOrden(Array):
	no_ordenado_de_mayor_a_menor = False
	no_ordenado_de_menor_a_mayor = False
	for i in range(1,len(Array)):
		if Array[i]>Array[i-1]:
			no_ordenado_de_mayor_a_menor=True
		if Array[i]<Array[i-1]:
			no_ordenado_de_menor_a_mayor=True
	if (not no_ordenado_de_menor_a_mayor) or (not no_ordenado_de_mayor_a_menor):
		return 1
	else:
		return 0