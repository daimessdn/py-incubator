# Program MencariNilaiTengah.py
# Menentukan nilai tengah dari suatu program
# Minimum/Selection Sort

from array import *

T = array('i', [12, 21, 15, 6, 31, 40])

if (len(T) > 1):
    for Pass in range(0, len(T)-1):
        # Tentukan nilai minimum antara dari Pass..len(T)-1
        IMin = Pass
        i = Pass + 1

        while (i < len(T)):
            if (T[IMin] > T[i]):
                IMin = i
            i += 1
            
        # i = len(T); IMin = index dengan nilai minimum
        # Tukar nilai T[IMin] dengan T[Pass] jika perlu
        if (IMin != Pass):
            Temp = T[Pass]
            T[Pass] = T[IMin]
            T[IMin] = Temp

# for x in range(0, len(T)):
#     print(T[x])

if(len(T) % 2 != 0):
    print(T[(len(T) - 1) // 2])
else:
    print((T[(len(T) // 2 - 1)] + T[(len(T) // 2)]) / 2)