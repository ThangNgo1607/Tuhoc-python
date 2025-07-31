# số hoàn thiện là một số nguyên dương mà tổng các ước nguyên dương chính thức của nó bằng chính nó. 
# Tìm tổng tất cả những số hoàn thiện trong phạm vi từ 1-1000.
tong = 0
for number in range(1,1000,1):
    s = 0
    for i in range(1,number,1):
        if number%i==0:
            s=s+i
    if s==number:
        tong=tong+s
print(tong)

# tìm tất cả các số hoàn thiện trong phạm vi từ 1-1000
for number in range(1,1000,1):
    s = 0
    for i in range(1,number,1):
        if number%i==0:
            s=s+i
    if s==number:
        print(s,end=" ")