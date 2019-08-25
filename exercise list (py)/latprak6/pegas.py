# 12217070
# Dimas Wihandono
# 1 Oktober 2018
# Latihan Praktikkum: Pengaruh gaya pegas
# Mencari koordinat suatu pegas dengan pendekatan Newton-Raphson

from math import *

def f(x):
	"""fungsi f(x)"""
	return sin(x) + (0.5 * sin(x)**2) - x
	
def f_aks(x):
	"""turunan f(x)"""
	return cos(x) + (cos(x) * sin(x)) - 1

def y(x):
	"""persamaan y"""
	return 0.5 * sin(x)

# input besaran x
x = 10

eps = 1E-6 # epsilon
x0  = 0   # definisi awal x0

while (abs(x - x0) > eps):
	x0 = x # x sebelumnya
	x = x0 - (f(x) / f_aks(x))

# x_aksen = round(x,5)
# y_aksen = round(y(x),5)

# print("(%d,%d)"%(x_aksen,y_aksen))

# koordinat = (round(x,5),round(y(x),5))

# print(koordinat)
	
print("(" + str(round(x,5)) + "," + str(round(y(x),5)) + ")")
