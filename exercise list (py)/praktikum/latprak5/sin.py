from math import *

# KAMUS
# x : float

# ALGORITMA
x = float(input(""))
n = 1  # tanda orde
i = -1 # tanda operasi negatif di awal
s = 0  # suku
jumlah = 0

while n <= 3:
	jumlah = jumlah + s
	i *= -1
	s = i * pow(x,n) / factorial(n)
	n += 2

#sum = x - pow(x,3)/factorial(3)

print(round(jumlah,5))