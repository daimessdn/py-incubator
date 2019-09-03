# fungsi array
# len(array): banyak elemen pada array
# array.append(obj)
# array.insert(index, obj)
# array.remove(obj): menghapus elemen
# array.index(obj): searching yang lain

# sorting
# binary search
# algoritma pengurutan ada ratusan
# counting sort, insertion sort, (selection sort), (bubble sort), heap sort, quick sort, merge sort, dll..

# Program SelectionSort1
# Mengurutkan array secara terurut membesar dengan Selection Sort

from array import *

# KAMUS
# T : array of integer
# Temp : integer
# Pass, K : integer, indeks

# ALGORITMA
# Asumsi : input array T telah dilakukan

N = int(input("Masukan banyak N: "))

T = array('i',[])

print("Masukan bilangan: ")
for i in range(0, N):
	ins = int(input(""))
	T.append(ins)

print("Hasil Selection Sort:")
# Bubble Sort - Algoritma Dasar
if (len(T) > 1):
	for Pass in range (0, len(T)-1):
		# Tentukan nilai minimum antara dari Pass sampai ujung paling belakang
		IMin = Pass
		whlie (i < len(T)):
			if (T[Imin ])

for K in range (0, len(T)):
	print(T[K])