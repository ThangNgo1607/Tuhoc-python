#Tính bao đóng (encapsulation): Trong class , sẽ luôn có các thuộc tính mà ta muốn cố định nó. Điều này ngăn chặn dữ liệu bị sửa đổi trực tiếp
class Bank():
    def __init__(self,hoten,cmt):
        self.hoten=hoten
        self.cmt=cmt
class Nhanvien(Bank):
    def __init__(self,hoten,cmt,):
        super().__init__(hoten,cmt)
        self.__luong = 5000  #sử dụng 2 dấu gạch dưới __ để gán private không cho phép truy cập từ bên ngoài


#TẠO CODE ĐỂ NGƯỜI CÓ THẨM QUYỀN TÁC ĐỘNG VÀO LƯƠNG:
    def get_luong(self):
        return self.__luong
    def set_luong(self,luong_moi):
        self.__luong=luong_moi

nv1=Nhanvien("Mai",123456)
nv2=Nhanvien("Ghi",123457)
print(nv1.hoten,nv1.cmt,)
print(nv2.hoten,nv2.cmt,)
 # thử tạo lương mới cho nhân viên 2 là: 7000 cú pháp như sau:
nv2.set_luong(7000)
print(f"luơng mới của nhân viên {nv2.hoten} là: {nv2.get_luong()}")
print(f"luơng mới của nhân viên {nv1.hoten} là: {nv1.get_luong()}")
