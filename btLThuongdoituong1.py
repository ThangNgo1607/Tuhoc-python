class Sinhvien():
    def __init__(self,hoten=str,ma_sv=int,que_quan=str):
        self.hoten=hoten
        self.ma_sv=ma_sv
        self.que_quan=que_quan
sv1=Sinhvien("Nguyen Van A",123,"Nghe An")
sv2=Sinhvien("Nguyen Van B",124,"Thanh Hoa")
sv3=Sinhvien("Nguyen Van C",125,"Ha Noi")
sv4=Sinhvien("Nguyen Van D",126,"Bac Giang")
print(f"Sinh viên 1 có tên là: {sv1.hoten}, quê ở {sv1.que_quan}")
print(f"Các sinh viên theo danh sách có quê lần lượt là:{sv1.que_quan,sv2.que_quan,sv3.que_quan,sv4.que_quan}")



