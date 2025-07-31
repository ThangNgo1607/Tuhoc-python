#viết chương trình để tạo ra một list có n phần tử, mà các phần tử phải là số ngẫu nhiên từ 1-100

from random import randrange

#cách 1: tạo một list có sẵn phần tử trong đó và cho nhân với n phần tử, sau đó dùng vòng lặp for và phương pháp thay thế phần tử
n = int(input("Mời phập và số phần tử trong list: "))
lst = [0]*n
print(lst)
for i in range(n):
    #print(i)
    lst[i]=randrange(1,101)
print(f"Chuỗi được tạo là: {lst}")


# cách 2: khởi tạo một list rỗng, sau đó tạo một list đưa vào list rỗng:
lst=[]
n = int(input("Mời phập và số phần tử trong list: "))
for _ in range(n):
    phantu = randrange(1,101)
    print(phantu)
    lst.append(phantu)
print(f"Chuỗi được tạo là: {lst}")