# Program segiempat
N = int(input()) # input N

# input karakter
C1 = str(input())
C2 = str(input())

if (N > 0):
	if (C1 != C2):
		for i in range(0, N):
			row = ""
			for j in range(0, N):
				if (i < j):
					row += C2
				else:
					row += C1
			print(row)
	else:
		print("Masukan tidak valid")
else:
	print("Masukan tidak valid")