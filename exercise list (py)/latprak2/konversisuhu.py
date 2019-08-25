# 12217070
# Dimas Wihandono
# 3 September 2018
# Latihan Praktikkum: Konversi Suhu
# Menampilkan suhu hasil konversi dari satuan derajat Celcius

# KAMUS
# t = float
# k = string / char

# ALGORITMA
t = float(input(""))
k = str(input(""))

if (k == "R"):
	print(format(4 * t / 5, "0.2f"))
elif (k == "F"):
	print(format((9 / 5 * t) + 32, "0.2f"))
elif (k == "K"):
	print(format(t + 273.15, "0.2f"))
