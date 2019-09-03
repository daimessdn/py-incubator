# 12217070
# Dimas Wihandono
# 2 September 2018
# Latihan Praktikkum: Deret Bilangan
# Menampilkan jumlah N bilangan pertama dengan N yang telah diinput sebelumnya

# KAMUS
# N, i,sum = int

# ALGORITMA
N = int(input(""))

sum = 0
for i in range (1, N+1):
	sum += i

print(sum)