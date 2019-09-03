# 12217070
# Dimas Wihandono
# 17 September 2018
# Program Selisih Dua Terbesar
# Menerima tiga buah input integer dan mengeluarkan hasil selisih bilangan terbesar dan terkecil

# KAMUS
# a, b, c, d : int
# hasil : fungsi deklarasi JumlahPecahan(a,b,c,d)

# subprogram FPB
def gcd(a,b):
	"Menentukan FPB dua bilangan"
	N = min(a,b)
	fpb = 1
	for i in range(1,N+1):
		if(a % i == 0 and b % i == 0):
		      fpb = i
	return fpb

def JumlahPecahan(pembilang1, penyebut1, pembilang2, penyebut2):
	"Menampilkan stringhasil penjumlahan pecahan"	
	hasilPemb = (pembilang1 * penyebut2) + (pembilang2 * penyebut1)
	hasilPeny = penyebut2 * penyebut1
	FPB = gcd(hasilPemb, hasilPeny)
	return str(int(hasilPemb/FPB)) + "/" + str(int(hasilPeny/FPB))
	
# ALGORITMA
a = int(input("Pembilang1 : "))
b = int(input("Penyebut1 : "))
c = int(input("Pembilang2 : "))
d = int(input("Penyebut2 : "))

hasil = JumlahPecahan(a,b,c,d)

print(hasil)
