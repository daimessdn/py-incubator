# 12217070
# Dimas Wihandono
# 1 Oktober 2018
# Newton Raphson
# Mencari pendekatan nilai f(x) = e^x + c^2 dengan galat eps = 0.000001

from math import *

def f(x):
	"""fungsi f(x)"""
	return exp(x) - x**2
	# return x**2 - 2
	
def f_aks(x):
	"""Turunan f(x)"""
	return exp(x) - 2 * x
	# return 2 * x

x = float(input(""))

eps = 1E-6 # epsilon
n   = 1    # iterasi ke-n
x0  = 0    # definisi awal x0

while (abs(x - x0) > eps):
	x0 = x # x sebelumnya
	x = x0 - (f(x) / f_aks(x))
	print(n, "%.6f"%(x))
	n = n + 1
