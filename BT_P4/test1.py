import math


def tinh(lis):
    global lis_ketqua
    c = 50
    h = 30
    for i in range(len(lis)):
        lis[i] = float(lis[i])
        lis_ketqua.append(math.sqrt((2 * c * lis[i]) / h))


st = input("Hay nhap vao mot chuoi gia tri: ")
#chuyen chuoi thanh list
lis = list(st.split(','))
lis_ketqua = []
tinh(lis)
print(lis_ketqua)