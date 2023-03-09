kq = 0
while True:
    s = input("Nhập nhật ký dao dịch: ")
    if s:
        #Chuyển chuỗi s thành lis trong đó lis có hai phần tử
        lis = [x for x in s.split( )]
        if (lis[0] == "D"):
            kq += int(lis[1])
        else:
            kq -= int(lis[1])
    else:
         break

print("Số tiền còn lại trong tài khoản: ", kq)

#VIDU:
#Giả sử đầu vào được cung cấp là: 
#D 300
#D 300
#W 200
#D 100
#Thì đầu ra sẽ là: 500

        