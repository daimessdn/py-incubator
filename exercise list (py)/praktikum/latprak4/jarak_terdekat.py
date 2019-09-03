# 12217070
# Dimas Wihandono
# 17 September 2018
# Program Jarak Terdekat
# Menerima kumpulan koordinat titik dan mengembalikan jarak dari dua titik terdekat.

# KAMUS
# absis, ordinat : array of integer
# hasil : fungsi deklarasi JumlahPecahan(a,b,c,d)

from math import *
from array import *

# subprogram jarak_terdekat
def jarak_terdekat(absis, ordinat):

	if (len(absis) < 2 or len(ordinat) < 2):
		return -1

	# elif (len(absis) == 2 and len(ordinat) == 2):
	# 	kuadratX = abs((absis[0]-absis[1])) * abs((absis[0]-absis[1])) #kuadrat-x
	# 	kuadratY = abs((ordinat[0]-ordinat[1])) * abs((ordinat[0]-ordinat[1])) # kuadrat-y
	# 	#resultan
	# 	kuadratTotal = kuadratX + kuadratY 
	# 	jarak = sqrt(kuadratTotal) 
		
	# 	return round(jarak,2)
	
	else:
		# for i in range(0, len(absis)):
		# 	print(absis[i])

		# for i in range(0, len(ordinat)):
			# print(ordinat[i])

		deltaX = array('d', [])
		deltaY = array('d', [])

		for i in range(0, len(absis)):
			x = abs(absis[i-1]-absis[i])
			deltaX.append(x)

			y = abs(ordinat[i-1]-ordinat[i])
			deltaY.append(y)

		jarak = sqrt(deltaX[0]**2 + deltaY[0]**2)
		for i in range(0,len(deltaX)):	
			if(jarak > sqrt(deltaX[i]**2 + deltaY[i]**2)):
				jarak = sqrt(deltaX[i]**2 + deltaY[i]**2)
			# print(jarak)


		return round(jarak,2)

# print(jarak_terdekat(array('i', [1,3,2,4]), array('i', [5,3,6,7])))
# print(jarak_terdekat(array('i', [4]), array('i', [7])))
# print(jarak_terdekat(array('i', [1,1]), array('i', [-1,-1])))
# print(jarak_terdekat(array('i', [1,2,10]), array('i', [3,4,10])))