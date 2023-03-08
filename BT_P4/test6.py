import math

def kiemtra(so_nhi_phan):
    so_thap_phan = 0
    for i in range(4):
        so_thap_phan += (so_nhi_phan % 10)*math.pow(2,i)
        so_nhi_phan = so_nhi_phan // 10
    return (so_thap_phan % 5 == 0)


st = input("Nhập một chuỗi các số nhị phân 4 chữ số: ")
lis = [int(x) for x in st.split(' ')]
print("Cac số chia hết cho 5: ")
for i in lis:
    if (kiemtra(i) == True):
        print(i)

