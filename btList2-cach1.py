#Viết chương trình nhập vào một danh sách, sau đó:
#1.Tạo ra một list mới bình phương các phần tử
#2.Xác định có bao nhiêu phần tử lớn hơn 50
#Giải:
#1:

n=int(input("Mời nhập vào số phần tử trong list: "))
lst=[0]*n
a=0
b=0
b2=0
for i in range(n):
    #print(i)
    a=a+1
    lst[i]=int(input(f"Mời nhập vào phần tử thứ {a}: "))
print(f"Danh sách được tạo sẽ là: {lst}")
lstnew=[]
for i in lst:
    binhphuong=i**2
    lstnew.append(binhphuong)
print(f"Danh sách mới sau khi bình phương sẽ là: {lstnew}")
#2:
'''for i in lstnew:
    if i>50:
        b=b+1
print(f"Có tổng số {b} phần tử lớn hơn 50")'''

# có thể mở rộng thêm đếm tổng số các phần tử nhỏ hơn 50 như sau:
for phtu in lstnew:
    if phtu > 50:
        b+=1
    elif phtu < 50:
        b2+=1
if b > 0 and b2>0:
    print(f"có {b} phần tử lớn hơn 50")
    print(f"có {b2} phần tử nhỏ hơn 50")