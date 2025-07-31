#Viết chương trình nhập vào một danh sách, sau đó:
#1.Tạo ra một list mới bình phương các phần tử
#2.Xác định có bao nhiêu phần tử lớn hơn 50
#Giải:

n=int(input("Mời nhập vào số phần tử trong list: "))
lst=[0]*n
a=0
b=0
for i in range(n):
    #print(i)
    a=a+1
    lst[i]=int(input(f"Mời nhập vào phần tử thứ {a}: "))
print(f"Danh sách được tạo sẽ là: {lst}")
for i in range(len(lst)):
    lst[i]=lst[i]**2
    if lst[i]>50:
        b=b+1
print(f"Danh sách mới sau khi bình phương sẽ là: {lst}")
print(f"Có tổng số {b} phần tử lớn hơn 50")
