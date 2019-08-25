# 12217070
# Dimas Wihandono
# 10 September 2018
# Duplikat Array
# Menampilkan nilai array yang memiliki nilai duplikat dengan catatan array dipastikan hanya memiliki sepasang nilai yang sama

from array import *

a = array('i', [])

N = int(input(""))

for i in range(0,N):
	x = int(input(""))
	a.append(x)

n = 0
found = False

while (not found and n < N):
	if (a.count(a[n]) >= 2):
		print(a[n])
		found = True
	n = n + 1
