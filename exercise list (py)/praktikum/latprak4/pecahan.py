# 12217070
# Dimas Wihandono
# 17 September 2018
# Subprogram Penjumlahan Pecahan
# Menerima masukan dua buah pembilang dan dua buah penyebut dan menuliskan hasil pecahan ke dalam bentuk yahng paling sederhana

# asumsi bahwa semua komponen pecahan lebih besar daripada nol

# subprogram FPB
def gcd(a,b):
	"Menentukan FPB dua bilangan"
	# KAMUS LOKAL
	# N, a, b, fpb, i : int

	# ALGORITMA SUBPROGRAM
	N = min(a,b)
	fpb = 1
	for i in range(1,N+1):
		if(a % i == 0 and b % i == 0):
		      fpb = i
	return fpb

def JumlahPecahan(pembilang1, penyebut1, pembilang2, penyebut2):
	"Menampilkan stringhasil penjumlahan pecahan"
	# KAMUS LOKAL
	# pembilang1, penyebut1, pembilang2, penyebut2, hasilPeny, hasilPemb : int
	# FPB : definisi penggunaan fungsi

	# ALGORITMA SUBPROGRAM	
	hasilPemb = (pembilang1 * penyebut2) + (pembilang2 * penyebut1)
	hasilPeny = penyebut2 * penyebut1
	FPB = gcd(hasilPemb, hasilPeny)
	return str(int(hasilPemb/FPB)) + "/" + str(int(hasilPeny/FPB))
