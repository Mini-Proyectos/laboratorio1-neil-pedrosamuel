def insertSort (Array):
	for i in range(1,len(Array)):
		key = Array[i]
		j=i-1
		while(j>=0 and Array[j]>key):
			Array[j+1] = Array[j]
			j = j - 1
		Array[j+1] = key
	print(Array)