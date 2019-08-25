# Program WujudAir.py
# Memberikan wujud air yang diketahui suhunya

# KAMUS
t = float(input("Masukkan suhu air (dalam derajat Celcius): "))

# ALGORITMA
if (t <= 0):
	print("beku")
elif (t >= 100):
	print("uap")
else:
	print("cair	")