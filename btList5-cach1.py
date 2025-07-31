#Viet chuong trinh in ra so lon thu 2 va so nho thu 2 trong List
lst=[]
n=int(input("Moi nhap vao so phan tu trong List: "))
dem=0
while dem<n:
    dem=dem+1
    phantu=int(input(f"Moi nhap vao phan tu thu {dem}: "))
    lst.append(phantu)
'''có thể dùng hàm for thay vì dùng hàm while:
lst = []
n = int(input("Mời nhập vào số phần tử trong List: "))
for i in range(n):
    phantu = int(input(f"Mời nhập vào phần tử thứ {i + 1}: "))
    lst.append(phantu)'''    
print(lst)
lst_max=[]
lst_min=[]
for i in lst:
    if i==max(lst):
        continue
    else:
        lst_max.append(i)
    if i==min(lst):
        continue
    else:
        lst_min.append(i)
print(lst_max)
print(lst_min)
index_phantulonthu2=[]
index_phantunhothu2=[]
for j in range(len(lst)):
    if lst[j]==max(lst_max):
        index_phantulonthu2.append(j)
        #print(index_phantu)
    elif lst[j]==min(lst_min):
        index_phantunhothu2.append(j)
print(f"so lon thu 2 trong List la: {max(lst_max)}")
print(f"Vi tri index so lon thu 2 trong List se la: {index_phantulonthu2}")
print(f"so nho thu 2 trong List la: {min(lst_min)}")
print(f"Vi tri index so nho thu 2 trong List se la: {index_phantunhothu2}")