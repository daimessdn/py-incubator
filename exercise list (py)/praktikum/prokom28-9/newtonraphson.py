from math import *

def f(x):
	return exp(x) - 5 * (x**2)	

def f_aksen(x):
	return exp(x) - 10 * x

epsilon1 = 0.0000001
epsilon2 = 0.000001

x = float(input("Masukan nilai x: "))

i = 0

x_sebelumnya = 0

# print(f(a), f(b), f(c))

while (abs(x-x_sebelumnya) > epsilon1):
	x_sebelumnya = x
	x = x - (f(x)/f_aksen(x))
	i += 1
	# print (a, b, c)
	# print(f(a), f(b), f(c))

print("Nilai x: " + str(round(x, 6)))
print("Iterasi " + str(i) + " kali")