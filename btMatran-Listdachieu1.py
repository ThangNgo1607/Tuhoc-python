# 1. Viết chương trình nhập vào ma trận có m dòng và n cột
# (m, n do người dùng nhập từ bàn phím). Các phần tử ngẫu nhiên
# từ (1 đến 100
from random import randrange
arr=[]
sodong=int(input("Moi nhap vao so dong: "))
socot=int(input("Moi nhap vao so cot: "))
for i in range(sodong):
    taomotdong=[]
    for j in range(socot):
        taomotdong.append(randrange(0,101))
    arr.append(taomotdong)
print(arr)
#Xuất ra kiểu ma trận:
'''for i in arr:
    for j in i:   
        print("{:<5}".format(j),end=" ")# cách nhau 3 dấu cách
    print()'''
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end="\t")
    print()


#Xuất dòng bất kỳ:
i = int(input("Moi nhap vao dong index can xuat ra: "))
print(f"Dong index thu {i} là: {arr[i]}")
# Xuất dòng ngẫu nhiên:
index=randrange(len(arr))
print(f"Dong index ngau nhien thu {index} là: {arr[index]}")
#tìm số lớn nhất trong ma trận list:
max=arr[0][0]
for i in range(sodong):
    for j in range(socot):
        if arr[i][j] > max: #So sánh phần tử hiện tại arr[i][j] với giá trị lớn nhất đang lưu trong max.
                            #Nếu arr[i][j] lớn hơn, thì cập nhật max.
            max = arr[i][j] #Ghi đè max bằng giá trị lớn hơn vừa tìm được.
print(f"So lon nhat trong ma tran la: {max}")
#tìm số nhỏ nhất trong ma trận list:
min=arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min: #So sánh phần tử hiện tại arr[i][j] với giá trị nhỏ nhất đang lưu trong min.
                            #Nếu arr[i][j] nhỏ hơn, thì cập nhật min.
            min = arr[i][j] #Ghi đè in bằng giá trị nhỏ hơn vừa tìm được.
print(f"So nho nhat trong ma tran la: {min}")
# Xuất ra cột bất kỳ:
b=int(input("Moi nhap vao vị tri index cot can xuat: "))
for c in range(len(arr)):
    print(arr[c][b])