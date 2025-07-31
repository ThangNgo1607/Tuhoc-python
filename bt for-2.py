# tính tổng S = 1! + 2! + 3! +.....+10!
n = 1
tong = 0
for i in range(1,11,1):
    #print(i)
    n = i*n
    #print(n)
    tong = tong + n
    #print(tong)
print("tong S =",tong)

'''for i in range(0,10):
    for j in range(i,9):
        print(j,end=" ")
    print()'''