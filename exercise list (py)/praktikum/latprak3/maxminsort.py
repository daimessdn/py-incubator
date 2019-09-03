# 12217070
# Dimas Wihandono
# 10 September 2018
# Definisi Array
# Menampilkan output nilai array berdasarkan indeks yang terdefinisi

from array import *

a = array('i', [])

cmd = str(input(""))

if (cmd == "a"):
	N = int(input(""))

	for i in range(0, N):
		x = int(input(""))
		a.append(x)
	
	max = a[0]

	for i in range(0, N):
		if (max < a[i]):
			max = a[i]

	print(max)

elif (cmd == "b"):
	N = int(input(""))

	for i in range(0, N):
		x = int(input(""))
		a.append(x)

	min = a[0]

	for i in range(0, N):
		if (min > a[i]):
			min = a[i]

	print(min)

elif (cmd == "c"):
	N = int(input(""))

	for i in range(0, N):
		x = int(input(""))
		a.append(x)

	if (len(a) > 1): 
		for Pass in range (0,len(a)-1):
			for K in range (len(a)-1,Pass,-1):
				if (a[K] < a[K-1]):
					Temp = a[K]
					a[K] = a[K-1]
					a[K-1] = Temp

	for i in range(0, N):
		print(a[i])

else:
	print("Masukan tidak valid")
