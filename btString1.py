# cho chuỗi sau a = "abchdABCDE". viết lại chuỗi a sao cho chữ thường thành chữ HOA và chữ hoa thành chữ thường

a = "abchdABCDE"
a1 = ""
for i in a:
    #print(i) 
    if i.islower(): # nếu i mà viết thường thì
        i = i.upper()  #i sẽ gắn bằng viết hoa
    else: # còn nếu i mà viết Hoa thì 
        i= i.lower() # i sẽ gắn bằng viết thường
    #print(i,end="")
    a1 = a1 + i
print(a1)

