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
		temp = C
		C = A
		A = temp
	else:
		temp = A
		A = B
		B = C
		C = temp
elif ((B < C) and (B < A)):
	if (C < A): # B < C < A
		temp = B
		B = C
		C = temp
	else: # B < A < C
		temp = C
		C = B
		B = A
		A = temp
else:
	if (A < B): # C < A < B
		temp = A
		A = B
		B = temp
	
print(str(A) + " " + str(B) + " " + str(C))