a ="English = 78 Sciece = 83 Math = 68 History = 65"
#1. tính tổng các số trong chuỗi trên
#2. Tính trung bình cộng
#giải bài 1:
#cách 1:
b = a.split(" ")
print(b)
c=int(b[2])+int(b[5])+int(b[8])+int(b[11])
print("tổng các số trong chuỗi a là: ",c)
#cách 2:
#sử dụng biến b trong cách 1:
tong = 0
dem = 0
for i in b:
    #print(i)
    if i.isdigit():
        tong = tong + int(i)
        dem += 1
print("tổng các số trong chuỗi a là: ",tong)

# bài 2:
print(f"Trung bình cộng của các môn học sẽ là: {tong/dem}")