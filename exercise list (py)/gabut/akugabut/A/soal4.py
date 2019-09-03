# Program Jumlah Deret
N = int(input()) # input N

# inisiasi
sum = 0
i = 0

# looping
while (sum <= N):
	num = int(input())
	sum += num
	i++         

print(i)
print(sum)