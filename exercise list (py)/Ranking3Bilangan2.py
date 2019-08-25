# Program Ranking3Bilangan.py
# Mengurutkan 3 buah bilangan dari besar ke kecil dengan asumsi semua bilangan berbeda

# KAMUS
A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
C = int(input("Masukkan nilai C: "))

# ALGORITMA
print("Urutan nilai besar ke kecil: ")
if ((A < B) and (A < C)):
	if (B < C):
		print (str(C) + " " + str(B) + " " + str(A))
	else:
		print (str(B) + " " + str(C) + " " + str(A))
elif ((B < C) and (B < A)):
	if (C < A):
		print (str(A) + " " + str(C) + " " + str(B))
	else:
		print (str(C) + " " + str(A) + " " + str(B))
else:
	if (A < B):
		print (str(B) + " " + str(A) + " " + str(C))
	else:
		print (str(A) + " " + str(B) + " " + str(C))

