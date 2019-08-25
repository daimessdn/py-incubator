# PROGRAM SIMNUM.PY
# APLIKASI SIMULASI DENGAN METODE NUMERIK
# CREATED BY KELOMPOK IV:
# # ANWAR SANTOSO                  12217026
# # SACHRUL WAHYU HIDAYAT          12217058
# # SHELLA SABIELAH MUTIARA        12217064
# # DIMAS WIHANDONO                12217070

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import math

# fungsi Lagrange sebagai fungsi untuk grafik interpolasi polinomial sekaligus mencari nilai prediksi pada x tertentu
def f(x1, z, n, x, y):
    """ Mengolah hasil nilai interpolasi pada nilai x1 """
    hasil = 0 # insisasi jumlah
    for i in range(0, z + 1):
        pi = 1 # inisiasi komponen Lagrage
        for j in range(0, z + 1):
            if (i != j):
                pi = pi * (x1 - x[j]) / (x[i] - x[j]);
    
        hasil = hasil + (y[i] * pi)

    return hasil

# fungsi Dranchuk-Abou Kaseem
def Dranchuk(Pr, Tr, Z):
    """ Mencari nilai f(Rhor) """
    # massa jenis
    Rho = 0.27 * Pr / (Z * Tr)
    
    # variabel-variabel
    R1 = 0.3265 + (-1.0700 / Tr) + (-0.5339 / Tr**3) + (0.01569 / Tr**4) + (-0.05165 / Tr**5)
    R2 = 0.27 * Pr / Tr
    R3 = 0.5475 + (-0.7361 / Tr) + (0.1844 / Tr**2)
    R4 = 0.1056 * ((-0.7361 / Tr) + (0.1844 / Tr**2))
    R5 = 0.6134 * Rho**2 / Tr**3

    return R1 * Rho + R3 * Rho**2 - R4 * Rho**5 + (R5 * (1 + 0.7210 * Rho**2)) * math.exp(-0.7210 * Rho**2) + 1 - Z  #Mengembalikan nilai f(Rhor)

# Fungsi turunan Dranchuk-Abou Kaseem
def Dranchuk_Derivative(Pr, Tr, Z, deltaZ):
    """ Mencari nilai turunan dari g(Z) dengan menggunakan metode gradien """
    return (Dranchuk(Pr, Tr, Z + deltaZ) - Dranchuk(Pr, Tr, Z)) / deltaZ  # Mengembalikan nilai turunan g(Z)

# fungsi menambah garis pada tabel
def tableLine(tableContent):
    # menampilkan border tabel
    line = ""

    for i in range(0, len(tableContent)-1):
        if (tableContent[i] == "|"):
            line += "+"
        else:
            line += "-"

    return line

# fungsi metode Newton-Raphson
def Newton_Rhapson(Z, Pr, Tr, MI, epsilon):
    """ Mencari solusi nilai Z dengan metode Newton Rhapson """
    m = 0
    Z0 = 0
    deltaZ = 0.001

    while (abs(Z - Z0) > epsilon and m < MI):
        Z0 = Z
        Z = Z - (Dranchuk(Pr, Tr, Z) / Dranchuk_Derivative(Pr, Tr, Z, deltaZ))
        m += 1

    return float(format(Z, "0.6f")) # Mengembalikan nilai Z dengan 6 angka di belakang koma

# beralih ke prosedur Modulus Young
def Young():
    """ Proses subprogram Modulus Young """

    # inisiasi list input
    L = []   # panjang setelah ditarik
    Lo = []  # panjang mula-mula
    F = []   # gaya tarikan
    A = []   # luas permukaan

    teg = []
    reg = []

    n = int(input("Masukan nilai n: "))

    for i in range(0,n):
        Lo.append(float(input("\nMasukan nilai Lo ke-" + str(i+1) + ": ")))
        L.append(float(input("Masukan nilai L ke-" + str(i+1) + ": ")))
        F.append(float(input("Masukan nilai F ke-" + str(i+1) + ": ")))
        A.append(float(input("Masukan nilai A ke-" + str(i+1) + ": ")))
   
    for i in range(0,n):
        reg.append((L[i]-Lo[i]) / Lo[i])
        teg.append((F[i] / A[i]))

    x1 = float(input("\nMasukan suatu nilai x: "))
    z = int(input("Masukan derajat polinom: "))

    # grafik interpolasi
    reg_x = np.arange(0, 1, 0.001)               # sumbu x
    ip = f(reg_x, z, n, reg, teg)                # sumbu y

    print("\nPerkiraan tegangan pada regangan x: " + str(format(f(x1, z, n, reg, teg), '0.5f')))
    # plt.plot(reg, ip)
    # plt.plot(x2, y2)
    plt.xlabel("regangan")
    plt.ylabel("tegangan")
    plt.title("Modulus Young")
    plt.scatter(reg, teg)
    plt.scatter(x1, f(x1, z, n, reg, teg), label='$x_{tebak}$')
    plt.plot(reg_x, ip)
    plt.legend()
    # plt.plot(reg_x, ip)
    plt.show()
    plt.savefig("record.png")

    return

# prosedur Gas Deviaton Factor (Season 1)
def DeviationFactor():
    Z = float(input("Masukan Z tebakan (Zk): "))
    Pr = float(input("Masukan nilai Pr: "))
    Tr = float(input("Masukan nilai Tr: "))
    epsilon = float(input("Masukan nilai galat: "))
    MI = int(input("Masukan jumlah iterasi: "))  # Iterasi maksimum

    print("Hasil perhitungan Z:")
    print(Newton_Rhapson(Z, Pr, Tr, MI, epsilon))

    return

# prosedur Gas Deviaton Factor (Season 1)
def DeviationFactor2():

    # Main program
    # Inisiasi list Pr, Tr, dan Z
    Pr = [] 
    Tr = []
    Z = []

    # input nilai Pr
    a = float(input("Masukan batas awal: ")) # nilai Pr pertama
    b = float(input("Masukan batas akhir: ")) # nilai Pr terakhir
    d = float(input("Masukan nilai interval: ")) # interval

    n = int(input("\nMasukan banyak Tr: "))


    for i in range(0,n):
        Tr.append(float(input("Masukan nilai Tr ke-" + str(i+1) + ": "))) # Menyimpan nilai Tr pada list Tr

    epsilon = float(input("Masukan nilai galat: "))

    MI = int(input("Masukan jumlah iterasi: ")) # iterasi maksimum

    i = a # inisiasi nilai i dengan nilai Pr pertama

    while (i < b):
        i += d # increment nilai i dengan nilai interval
        Pr.append(i) # Menyimpan nilai i pada list Pr

    Zm = 1

    # inisiasi tabel Z
    for i in range(0,n):
        Z.append([])
        for j in range(0,len(Pr)):
            Z[i].append(Newton_Rhapson(Zm, Pr[j], Tr[i], MI, epsilon))
        # print(Z[i])

    # menampilkan tabel
    print("\nTABEL GAS-DEVIATION FACTOR\n")
    for j in range(0, 3):
        if (j == 0 or j == 1):
            tableContent = "| "
            tableContent += "   Pr/Tr | "
            for k in range(0, n):
                tableContent += format(Tr[k],  "0.6f") + " | "
            if (j == 1):
                print(tableContent)

            print(tableLine(tableContent))

        else:
            for i in range(0,len(Pr)):
                tableContent = "| "
                tableContent += format(Pr[i], "0.6f") + " | "
                for k in range(0, n):
                    if(Z[k][i] > 0):
                        tableContent += format(Z[k][i],  "0.6f") + " | "
                    else:
                        tableContent += format(Z[k][i],  "0.5f") + " | "
                print(tableContent)

                print(tableLine(tableContent))

    # grafik
    for i in range(0,n):
        plt.plot(Pr, Z[i], label=('Tr = ' + str(Tr[i])))

    plt.xlabel("Pr") # memberikan keterangan pada sumbu x
    plt.ylabel("gas deviation factor, Z") # memberikan keterangan pada sumbu y
    plt.title("Gas Deviation Factor")
    plt.legend() # Menampilkan legenda dari grafik
    plt.show() # Menampilkan grafik dalam format gambar
    plt.savefig("Dranchuk.pdf")

    return

p = "\nPilihan menu: \n1. Modulus Young \n2. Gas Deviation Factor (1) \n3. Gas Deviation Factor (2) \n4. Keluar \n"

print("SELAMAT DATANG DI PROGRAM SIMNUM")
print("PROGRAM SIMULASI NUMERIK")
print("KAMI MEMBUAT SUATU PROGRAM MENGGUNAKAN SIMULASI NUMERIK")

print(p)

a = int(input('Masukan pilihan menu: '))

# selama pengguna tidak menginput nilai 4, program akan terus berjalan
while(a != 4):
    # Modulus Young
    if(a == 1):
        Young()

    # Gas Deviation Factor #1
    elif (a == 2):
        DeviationFactor()

    # Gas Deviation Factor #2
    elif(a == 3):
        DeviationFactor2()
    
    else:
        print("Masukan pilihan tidak berlaku.\n")

    print(p)
    a = int(input('Masukan pilihan menu: '))

# some credits and closing sentences
print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI")
print(" _____    _____    _____ ")
print("|     |  |     |  |     |")
print("|  x  |  |  x  |  |  x  |")
print("|   __|  |     |  |  x  |  __  __   _    _   __  ")
print("|  |     |  |\\ \\  |  x  | |   |  | | \\  / | |__| ")
print("|__|     |__| \\_\\ |_____| |__ |__| |  \\/  | |    ")
print("\nCONTRIBUTORS:")
print("ANWAR SANTOSO            12217026")
print("SACHRUL WAHYU HIDAYAT    12217058")
print("SHELLA SABIELAH MUTIARA  12217064")
print("DIMAS WIHANDONO          12217070")
print("\nCopyright (C) ProComp Corporation (2018), All right reserved.")