
# program SumNBilangan.py
# membuat prosedur yang menerima input N buah bilangan dan menampilkan hasil penjumlahan N bilangan

# KAMUS UTAMA
# a, b = int

N = int(input("Masukan N bilangan: "))

def SumNBil (N):
	"Menampilkan hasil jumlah N bilangan"

	# KAMUS LOKAL
	# sum, i = int

	# ALGORITMA LOKAL
	sum = 0
	for i in range (0, N):
		sum += int(input("Masukan bilangan ke-" + str(i+1) + ": "))

	# cetak hasil
	print("Hasil penjumlahan: " + str(sum))
	return

# ALGORITMA PROGRAM UTAMA
SumNBil(N)