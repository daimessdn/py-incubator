# 12217070
# Dimas Wihandono
# 17 September 2018
# Subprogram Pemangkatan
# Menerima masukan dua buah integer a dan b dan menuliskan pangkat b dari a ke layar

def HitungPangkat (x,y) :
	# Mengembalikan nilai integer hasil penghitungan pangkat y dari x
	# KAMUS LOKAL
	# x, y, pangkat: int
	# Algoritma
	pangkat = 1
	if (y != 0):
		for i in range(0,y):
			pangkat = pangkat * x
	return pangkat
