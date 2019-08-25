# Program TotalBilangan.py
# menampilkan jumlah total dari 10 buah bilangan

# KAMUS
# i, N, sum = int

# ALGORITMA
N = int(input("Masukkan N mahasiswa: "))
sum = 0
for i in range(1, N+1):
	data = int(input("Masukkan nilai mahasiswa ke-" + str(i) + ": "))
	sum += data
avg = float(sum) / float(N)
print("Rata-rata kelas:")
print(avg)