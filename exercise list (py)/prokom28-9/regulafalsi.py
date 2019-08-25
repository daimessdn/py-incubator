from math import *

def f(x):
	return exp(x) - 5 * (x**2)	

epsilon1 = 0.00001
epsilon2 = 0.000001

a = float(input("Masukan nilai a: "))
b = float(input("Masukan nilai b: "))

i = 0

# print(f(a), f(b), f(c))

while (abs(a-b) > epsilon1):
	c = b - (f(b)*(b-a)/(f(b)-f(a)))
	if (abs(f(c)) < epsilon1):
		b = c
		a = c
	else:
		if (f(a) * f(c) < 0):
			b = c
		else:
			a = c
	i += 1
	# print (a, b, c)
	# print(f(a), f(b), f(c))

print("Nilai c: " + str(round(c, 6)))
print("Iterasi " + str(i) + " kali")