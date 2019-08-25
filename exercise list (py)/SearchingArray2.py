from array import *

# KAMUS
# X, i = int
# found = bool
# search = array[0:N]

# ALGORITMA

X = int(input("Masukan nilai X: "))

# definisi array
search = array('i', [1,2,3,5,6])

# definisi awal nilai
found = False
i = 0

while (found != True and i < len(search)):
	if(X < search[i]):
		# print(str(search[i]) + " terdapat pada indeks ke-" + str(i))
		found = True
	else:
		i = i + 1
	
# cetak hasil	
if (found == False):
	print(" Tidak ada yang lebih besar dari " + str(X))
else:
	print(str(search[i]) + " terdapat pada indeks ke-" + str(i))