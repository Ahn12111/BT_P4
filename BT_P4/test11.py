st = input("Nhap mot day so, cach nhau khoang trang: ")
#Chuyển string thành lis và nếu phần tử đang được xét không chia hết cho 2 thì đưa vào lis
lis = [x for x in st.split( ) if int(x) % 2 != 0]
print(" ".join(lis))

#VIDU:
#Nhap mot day so, cach nhau khoang trang: 1 2 3 4 5 6
#1 3 5
