#Chuong trinh nhap vao username va pass, neu user k co trong danh sach thi bao user khong ton tai, neu user dung vaf bao pass sai thi bao
#mat khau sai, neu user dung va pass dung thi bao dang nhap thanh cong
# neu người dùng nhập lại tối đa 5 lần, nếu sai user hoặc mật khẩu thì sẽ bị khóa tài khoản:

dic={"user1":"abcd3r","user2":"ab2der","user3":"ab2der","user4":"a5cder"}

dem = 0
max_sai = 5

while dem < max_sai:
    username = input("Mời nhập user: ")
    password = input("Mời nhập pass: ")

    if username not in dic:
        print("Không tồn tại user")
        dem += 1
    
    else:
        if password != dic[username]:
            print("Mật khẩu sai rồi")
            dem += 1
        else:
            print("Bạn đã đăng nhập thành công")
            break

if dem == max_sai:
    print("Tài khoản đã bị khóa do nhập sai quá nhiều lần!")