# Program TotalBilangan.py
# menampilkan jumlah total dari 10 buah bilangan

# KAMUS
# i, N, sum = int

# ALGORITMA
print ("Masukkan bilangan (selain -999)")
ganjil = 0
genap = 0
pos = 0
neg = 0
N = int(input(""))
while (N != -999):
	if (N == 0):
		genap +=1
	else:
		if (N > 0):
			pos += 1
		else:
			neg += 1
		if (N % 2 == 0):
			genap += 1
		else:
			ganjil += 1
	N = int(input(""))
print ("Banyak bilangan ganjil: " + str(ganjil))
print ("Banyak bilangan genap: " + str(genap))
print ("Banyak bilangan positif: " + str(pos))
print ("Banyak bilangan negatif: " + str(neg))