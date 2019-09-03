# 12217070
# Dimas Wihandono
# 3 September 2018
# Latihan Praktikkum: Gambar Pola
# Menampilkan gambar pola dari indikator N, C1, dan C2

# KAMUS
# N = int
# C1, C2 = str

# ALGORITMA
N = int(input(""))
C1 = str(input(""))
C2 = str(input(""))

if (N <= 0 or C1 == C2):
	print ("Masukan tidak valid")
else:
	for i in range(0, N):
		row = ""
		for j in range(0, N):
			if (i == 0 or i == N-1 or j == 0 or j == N-1):
				row = row + C1
			else:
				row = row + C2
		print(row)
