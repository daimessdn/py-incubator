# Program NilaiTengah.py
# Menampilkan nilai tengah dari data yang sudah diurutkan

from array import *

# KAMUS
# T : array of integer
# Temp : integer
# Pass, K : integer, indeks

# ALGORITMA
# Asumsi : input array T telah dilakukan

# input
N = int(input("Masukan banyak N: "))

# definisi array
T = array('i',[])

# pengisian array
print("Masukan bilangan: ")
for i in range(0, N):
	ins = int(input(""))
	T.append(ins)

print("Hasil data setelah diurutkan:")
# Proses sorting dengan bubble sort dan menampilkan
if (len(T) > 1):
	for Pass in range (0, len(T)-1):
		for K in range (len(T)-1, Pass, -1):
			if (T[K] > T[K-1]):
				Temp = T[K]
				T[K] = T[K-1]
				T[K-1] = Temp

# menampilkan array yang sudah terurut
for K in range (0, len(T)):
	print(T[K])

# mencari nilai tengah
print("Nilai tengah:")
if (len(T) % 2 != 0):
	print(float(T[int(((len(T) - 1) / 2))]))
else:
	print(float((T[int((len(T)/2)-1)] + (T[(int(len(T)/2))])) / 2))