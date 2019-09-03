# 12217070
# Dimas Wihandono
# 1 Oktober 2018
# Latihan Praktikkum: Bisection - Regulafalsi
# Mencari pendekatan nilai f(x) = x^3 + 4x - 10 dengan pendekatan bisection atau regulafalsi (salah satunya)

from math import *
from decimal import *

def f(x):
	"""fungsi f(x)"""
	return x**3 + 4 * x - 10
	# return x**3 + 2 * x - 8
	
cont = str(input("")) # input perintah

# interval a dan b
a = Decimal(float(input("")))
b = Decimal(float(input("")))

eps1 = 0.000001       # epsilon 1
eps2 = 0.00000001     # epsilon 2
n    = 0              # iterasi ke-n

if (cont == "b"):     # bisection
	while (abs(a - b) > eps1 or f(c) > eps2):
		c = (a + b) / 2
		if (f(a) * f(c) < 0):
			b = c
		else:
			a = c
		print("%d %.6f"%(n,c))
		n = n + 1
elif (cont == "rf"):   # regula-falsi
	while (abs(a - b) > eps1):
		c = b - ((f(b) * (b - a))/(f(b) - f(a)))
		if (abs(f(c)) < eps2):
			a = c
			b = c
		else:
			if (f(a)*f(c) < 0):
				b = c
			else:
				a = c
		print("%d %.6f"%(n,c))
		n = n + 1
