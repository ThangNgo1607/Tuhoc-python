#xuất chuỗi theo vị trí index, index vị trí của chuỗi bắt đấu từ 0
t = "123456789"
print(t[1:7:2]) #-> truy xuất từ vị trí 1 đến 6 bước nhảy là 2: 246
print(t[3]) #-> truy xuất vị trí thứ 3 của chuỗi: 4
print(t[3:6]) #-> truy xuất từ vị trí thứ 3 đến vị trí < 6 của chuỗi: 456
print(t[3:]) #-> truy xuất từ vị trí thứ 3 đến hết chuỗi: 456789
print(t[:3]) #-> Truy xuất từ đầu đến vị trí < 3 của chuỗi: 123
print(t[::-1]) # đảo ngược chiều chuỗi: 987654321
s=""
for i in range(len(t)): #xuất các vị trí số lẻ
    if i%2!=0:
        #print(t[i],end=" ")
        s=s+" "+t[i]
print(s)        