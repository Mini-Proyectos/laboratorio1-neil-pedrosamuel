def binarySearch(left,right,x,Array):
	while(left<right):
		mid= int((left+right)//2)
		if(x==Array[mid]):
			print("El elemento %s se encuentra en la posicion %s" % (x, mid+1))
			return 0
		if(x<Array[mid]):
			right=mid-1
		else:
			left=mid+1
	print('No se encontro el elemento \n')
	return 0