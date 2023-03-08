st = input("Nhập vào một chuỗi gồm các từ: ")
#Chuyển chuỗi về dạng set để loại bỏ những từ trùng lặp (vì set là một tập hợp các phần tử không lặp nhau)
set1 = set(st.split(' '))
#Chuyển về list để sắp xếp
lis = list(set1)
lis.sort()
print("Chuỗi sau khi loai bỏ các từ trùng lặp và xắp xếp theo bảng chữ cái: ")
for i in lis:
    print(i, end = ' ')


#VIDU:
#Nhập vào một chuỗi gồm các từ: hello world and practice makes perfect and hello world again
#Kết quả:
#Chuỗi sau khi loai bỏ các từ trùng lặp và xắp xếp theo bảng chữ cái:
#again and hello makes perfect practice world