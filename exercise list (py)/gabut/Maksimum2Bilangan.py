# Program Maksimum2Bilangan.py
# Membuat fungsi yang menerima dua buah inputan dan mencetak bilangan terbesar di antara keduanya

# KAMUS
# a, b = int

def Maks2Bil (a, b):
	"Menentukan dua bilangan terbesar di antara keduanya"

	# KAMUS LOKAL
	# a, b = int

	# ALGORITMA SUBPROGRAM
	if (a > b):
		return a
	else:
		return b

# ALGORITMA PROGRAM UTAMA
a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukan bilangan kedua: "))

hasil = Maks2Bil (a, b)

print ("Bilangan terbesar: " + str(Maks2Bil(a, b)))