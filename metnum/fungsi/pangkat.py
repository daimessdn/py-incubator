def pangkat(x,n):
    hasil = 1
    if (n == 0 and x is not 0):
        hasil = 1
    elif (x == 0):
        hasil = 0
    else:
        for i in range(1,n+1):
            hasil *= x
    return hasil