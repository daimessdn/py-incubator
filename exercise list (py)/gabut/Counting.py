L = [1,2,3,3,6]
x = int(input("Masukkan sebuah angka: "))

count = 0
# for i in range(0, len(L)):
# 	if (L[i] == x):
# 		count += 1

for i in L:
	if (i == x):
		count += 1

print("x muncul " + str(count) + " kali di L")