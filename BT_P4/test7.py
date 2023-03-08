def kiemtra(so):
    for i in range(4):
        if ((so % 10) % 2 != 0):
            return False
        so = so // 10
    return True

for i in range(1000,3001):
    if (kiemtra(i) == True):
        print(i, end = ',')
