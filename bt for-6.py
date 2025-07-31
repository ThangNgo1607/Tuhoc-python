# vẽ hình trái tim
for i in range(0,7):
    for j in range(0,7):
        if (i==0 and j in(1,2,4,5)) or (i==1 and j in(0,3,6)) or (i==2 and j in(0,6)) or (i==3 and j in(1,5)) or (i==4 and j in(2,4)) or (i==5 and j==3):
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print("")

# vẽ hình ô vuông:
for i in range(1,7):
    for j in range(7):
        if j in (1, 2, 5, 6) or (i in (1, 2, 5, 6) and j in (3, 4)):
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()
print("_"*20)
            
for i in range(1,7):
    for j in range(7):
        if j in (0, 1, 4, 5) or (i in (1, 2, 5, 6) and j in (2, 3)):
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()      