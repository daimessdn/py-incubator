# Program TotalBilangan.py
# menampilkan jumlah total dari 10 buah bilangan

# KAMUS
# i, N, sum = int

# ALGORITMA
sum = 0
for i in range (1, 11):
	N = int(input("Masukkan bilangan ke-" + str(i) + ": "))
	sum += N
print(sum)