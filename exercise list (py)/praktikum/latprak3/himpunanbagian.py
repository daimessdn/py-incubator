# 12217070
# Dimas Wihandono
# 10 September 2018
# Himpunan Bagian
# Mengecek apakah himpunan A merupakan himpunan bagian himpunan B atau tidak

from array import *

A = array('i', [])
B = array('i', [])

NEffA = int(input(""))

for i in range(0,NEffA):
	x = int(input(""))
	A.append(x)

NEffB = int(input(""))

for i in range(0,NEffB):
	x = int(input(""))
	B.append(x)

n = 0
subset = True

while (n < NEffA and subset == True):
	a = A.count(A[n])
	b = B.count(A[n])
	if (a != b):
		subset = False
	n = n + 1

if (subset == True):
	print("YA")
else:
	print("TIDAK")
