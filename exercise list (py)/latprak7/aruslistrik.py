# 12217070
# Dimas Wihandono
# 22 Oktober 2018
# Rangkaian Listrik
# menerima input berupa 4 buah nilai V dan mengeluarkan matriks A dan B yang telah tereliminasi dengan pembulatan dua angka di belakang koma

# kamus
# A = matriks float
# B = vektor float
# i, j, k = int
# m = float
# n = int

# inisiasi matriks
A = [[3, -1, 0, -1],
	[-1, 3, -1, 0],
	[0, -1, 3, -1],
	[-1, 0, -1, 3]
]

B = []

# inisiasi matriks solusi
X = [0, 0, 0, 0]

n = len(A)

# pengisian matriks B
for i in range(0,n):
	B.append(float(input("")))

# metode Gauss Naif
# memulai dari baris pivot 0 hingga n
for k in range(0, n):
	# eliminasi mulai dari baris k+1 hingga baris ke-n
	for i in range(k+1, n):
		# mencari faktor pengali
		m = float(A[i][k] / A[k][k])
		# eliminasi elemen dari kolom k hingga kolom ke-n
		for j in range(k, n):
			A[i][j] = A[i][j] - (m*A[k][j])
		# eliminasi elemen vektor B pada baris i		
		B[i] = B[i] - (m*B[k])		

# mencetak hasil matriks segitiga
print("[")
for i in range(0,n):
	print("[")
	for j in range(0,n):
		print(format(A[i][j], "0.2f"))
	print("]")
print("]\n")

# mencetak hasil matriks B tereliminasi
print("[")
for i in range(0,n):
	print(format(B[i], "0.2f"))
print("]")
