# Program Pangkat2
# Menerima masukan sebuah integer dan
# menuliskan pangkat 2 dari nilai tersebut ke layar

# kamus
# y, hasil = int
#
# definisi pangkat
def Pangkat2 (x):
	"Menghasilkan pangkat 2 dari x"
	# ALGORITMA
	return x*x

# algoritma program utama
y = int(input("Masukan sebuah angka: "))
hasil = Pangkat2(y)
print("Hasil pangkat:")
print(hasil)