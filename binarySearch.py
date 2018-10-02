import sys

def bs(l,r,x,A):

	while(l<r):
		mid= int((l+r)//2)
		if(x==A[mid]):
			return mid
		if(x<A[mid]):
			r=mid-1
		else:
			l=mid+1

	return -1

def vo(A):
	nomaymenor = False
	nomenormayor = False
	for i in range(1,len(A)):
		if A[i]>A[i-1]:
			nomaymenor=True
		if A[i]<A[i-1]:
			nomenormayor=True
	if (not nomenormayor) or (not nomaymenor):
		return 1
	else:
		return 0


A = []

name = sys.argv[1]

x = int(sys.argv[2])

archivo = open(name,'r+')

while True:
	linea = archivo.readline()
	if not linea:
		break
	A.append(int(linea))

archivo.close

if(vo(A)):

	ans = bs(0,len(A),x,A)

	if(ans==-1):
		print("No se encontro el el elemento.\n")
	else:
		print("El elemento %s se encuentra en la posicion %s\n" % (x, ans+1))

else:

	print("El arraglo no esta ordenado. \n")