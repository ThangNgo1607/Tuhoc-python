a = input("Thiết lập mật khẩu: ")
while True:
    x = bool
    y = bool
    for i in a:
        if i.isdigit():
            x = True
            break
        else:
            x = False
    for i in a:
        if i.isalpha():
            y = True
            break
        else:
            y = False
    print(x,y)

    if len(a)<6 or x==False or y==False:
        a = input("Mời thiết lập lại mật khẩu, mật khẩu phải có 6 ký tự trở lên, có số hoặc chữ trong mật khẩu: ")    
    else:
        print("Mật khẩu đã hợp lệ")
        break
dem = 0
b = input("mời người dùng nhập lại mật khẩu: ")
while b!=a:
    dem+=1
    b = input(f"Nhập lại mật khẩu, bạn đã nhập sai {dem}/5 lần: ")
    if dem==5:
        print("Bạn đã nhập sai quá 5 lần, bạn thua rồi")
        break
else:
    print("Chúc mừng bạn, bạn đã đúng rồi!")

