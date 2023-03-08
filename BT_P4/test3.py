st = input("Nhập một chuỗi gồm các từ: ")
# đưa chuỗi st về thành list với mỗi phần tử là một từ cách nhau bởi dấu phẩy
lis = list(st.split(','))
#sắp xếp các từ theo bảng chữ cái
lis.sort()
print("Sap xep cac tu theo bang chu cai: ", lis)

#Vi du:
#Nhập một chuỗi gồm các từ: without,hello,bag,world
#Kết quả:
#Sap xep cac tu theo bang chu cai:  ['bag', 'hello', 'without', 'world']