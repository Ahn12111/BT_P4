chu = 0
so = 0
st = input("Nhập một chuỗi gồm số và chữ: ")
for i in st:
    if (('a' <= i <= 'z') or('A' <= i <= 'Z')):
        chu += 1
    if ('1' <= i <= '9'):
        so += 1
print("Số chữ cái là: ", chu)
print("Số chữ số là: ", so)

#Vidu:
#hello world! 123
#Số chữ cái là: 10 Số chữ số là: 3