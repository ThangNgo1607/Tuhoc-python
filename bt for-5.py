'''vẽ chữ N'''
n=int(input("mời nhập vào số n = "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or j==i:
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()

for i in range(0,10):
    for j in range(0,10):
        if j==0 or j==9 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

        

    