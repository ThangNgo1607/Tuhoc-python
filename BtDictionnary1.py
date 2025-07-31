#Chuong trinh nhap vao username va pass, neu user k co trong danh sach thi bao user khong ton tai, neu user dung vaf bao pass sai thi bao
#mat khau sai, neu user dung va pass dung thi bao dang nhap thanh cong

dic={"user1":"abcd3r","user2":"ab2der","user3":"ab2der","user4":"a5cder"}

username = input("Mời nhập user: ")
password = input("Mời nhập pass: ")

if username not in dic:
    print("Không tồn tại user")
else:
    if password != dic[username]:
        print("Mật khẩu sai rồi")
    else:
        print("Bạn đã đăng nhập thành công")