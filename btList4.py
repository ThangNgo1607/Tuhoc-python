#Viết chương trình nhập vào một List, đếm xem trong list có bao nhiêu số nhỏ hơn 5 và vị trí các số đó
n=int(input("Mời nhập vào số phần tử n: "))
lst=[0]*n
a=0
for i in range(n):
    #print(i)
    a+=1
    lst[i] = int(input(f"mời nhập vào phần tử thứ {a}: "))
print("List vừa được tạo sẽ là: ",lst)
lst_index=[]
dem=0
for j in range(len(lst)):
    if lst[j]<5:
        dem += 1
        lst_index.append(j)
print(f"Có {dem} phần tử nhỏ hơn 5")
print(f"Vị trí các phần tử nhỏ hơn 5 lần lượt là: {lst_index}")