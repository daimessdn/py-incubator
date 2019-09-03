# Program klasifikasi bilangan
N = int(input())

# inisiasi bilangan
pos = 0
net = 0
neg = 0

# looping
for i in range(0,N):
	num = int(input())

	# pengolahan data (validasi)
	if (num > 0): 		# bilangan positif
		pos += 1  		# atawa pos = pos + 1
	elif (num == 0):	# bilangan netral
		net += 1		# atawa net = net + 1
	else:
		neg += 1

print(neg)
print(net)
print(pos)