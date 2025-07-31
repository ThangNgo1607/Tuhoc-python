#cho một ma trận matrix, hãy xuất ma trận ra màn hình:
matrix=[
    [12,5,7,],
    [4,6,3],
    [123,7,9]
]
for dong in matrix: # duyệt từng phần tử trong matrix
    #print(dong)
    for hang in dong:   #duyệt từng phần tử trong hàng
        print("{:<5}".format(hang),end=" ")  # "{:<5}" có nghĩa là căn trái số (<) và chừa 5 ký tự độ rộng cho nó.
        #end=" " giúp các số in ra nằm trên cùng một dòng, ngăn cách bằng dấu cách thay vì xuống dòng. 
    print() #Sau khi in xong một dòng (1 hàng ngang trong ma trận), thì in một dòng trắng để xuống dòng — chuẩn bị cho dòng tiếp theo.




from random import randrange
#tạo một List đa chiều có dòng và cột cho trước:
arr=[]
dong=4
cot=3
for i in range(dong):
    taomothang=[]
    for j in range(cot):
        taomothang.append(randrange(0,21))
    arr.append(taomothang)
print(arr)
    
    
    #xuất ra ma trận(cách 1):
for dong in arr:
    for hang in dong:   
        print("{:<5}".format(hang),end="   ")# cách nhau 3 dấu cách
    print()
print("_"*20)
   
   
    #xuất ra ma trận(cách 2):
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end="\t") #giúp các số in ra nằm trên cùng một dòng, ngăn cách bằng 1 tab thay vì xuống dòng. 
    print()
