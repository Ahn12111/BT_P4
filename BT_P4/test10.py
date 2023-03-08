def tinh(a):
    s = 0
    x = a
    for i in range(4):
        s = s + x
        x = x * 10 + a
    return s

a = int(input("Nhập a: "))
print("ket qua: ", tinh(a))

#Yêu cầu: tính giá trị của a+aa+aaa+aaaa
#VIDU:
#Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
