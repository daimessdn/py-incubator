# 12217070
# Dimas Wihandono
# 24 September 2018
# Hampiran MacLaurin
# Menghitung hasil dari f(x) = sin x sampai orde ketiga persamaan MacLaurin

import math

# KAMUS
# i : int
# x, sum, orde = float

# ALGORITMA

# def factorial(a):
#	fact = 1
#	for i in range(0,i+1):
#		if (i == 0):
#			fact *= 1
#			print(fact)
#		else:
#			fact *= i
#			print(fact)
#	return fact

# print(factorial(3))
# print(factorial(5))

x = float(input(""))
i = 0
sum = 0
count = 1

while(i <= x):
	if(i == 0):
		orde = 1
	else:
		# print (pow(0.2,i), math.factorial(i))
		if (count % 2 == 0):
			orde = -1 * float(pow(0.2,i) / math.factorial(i))
		else:
			orde = float(pow(0.2,i) / math.factorial(i))
	# print (orde)
	sum += orde
	i += 2
	count += 1

if (sum <= 2):
	print(sum)
else:
	print(format(sum, '0.16f'))
