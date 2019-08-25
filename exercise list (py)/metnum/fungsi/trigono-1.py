from math import *
from phytagoras import phytagoras

a = float(input("Input sisi a: "))
b = float(input("Input sisi b: "))

c = phytagoras(a,b)

print("Sisi hipotenusa:")
print(str(c) + "\n")

print("sin = " + str(format(a / c, "0.3f")))

print("cos = " + str(format(b / c, "0.3f")))

print("tan = " + str(format(a / b, "0.3f")))

print("cot = " + str(format(b / a, "0.3f")))

print("sec = " + str(format(c / b, "0.3f")))

print("csc = " + str(format(c / a, "0.3f")))