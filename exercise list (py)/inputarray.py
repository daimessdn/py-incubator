from array import *

x = array('i', [])

N = int(input("Masukan banyak baris: "))

for i in range(0,N):
	ip = int(input("Masukan indeks ke-" + str(i+1) + ": "))
	x.append(ip)

# while (i >= 0):
# 	print(x[i])
# 	i = i - 1

for i in range(N-1, -1, -1):
	print(x[i])