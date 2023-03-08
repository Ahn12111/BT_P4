up = 0
low = 0
st = input("Nhập một chuỗi: ")
for i in st:
    if i.isupper():
        up += 1
    if i.islower():
        low += 1
print("Chữ hoa: ", up)
print("Chữ thường: ", low)

#VIDU:
#đầu vào là: Cafedev – Kênh Thông Tin IT
#Thì đầu ra là:
#Chữ hoa: 7
#Chữ thường: 15