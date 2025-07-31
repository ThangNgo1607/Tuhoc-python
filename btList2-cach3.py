#Viết chương trình nhập vào một danh sách, sau đó:
#1.Tạo ra một list mới bình phương các phần tử
#2.Xác định có bao nhiêu phần tử lớn hơn 50
#Giải:

n=int(input("Mời nhập vào số phần tử trong list: "))
lst=[]
dem = 0
while dem<n:
    dem=dem+1
    a=int(input("Mời nhập vào phần tử: "))
    lst.append(a)
print(f"List được tạo sẽ là: {lst}")
lst2=[]
for i in lst:
    phantu=i**2
    lst2.append(phantu)
print(f"List được tạo mới sau khi bình phương sẽ là: {lst2}")
b=0
for i in lst2:
    if i>50:
        b=b+1
print(f"Có tổng số {b} phần tử lớn hơn 50")