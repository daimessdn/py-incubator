def selisihTerbesar(x,y,z):
	"Mengembalikan nilai selisih bilangan terbesar dan nilai terkecil"
	# KAMUS LOKAL
	# x, y, z: int
	# ALGORITMA SUBPROGRAM
	if (x < y and x < z):
		if (y < z): # x < y < z
			return z - x
		else: # x < z < y
			return y - x
	elif (y < x and y < z):
		if (x < z): # y < x < z
			return z - y
		else: # y < z < x
			return x - y
	else: # z < (x & y)
		if (x < y): # z < x < y
			return y - z
		else: # z < y < x
			return x - z

