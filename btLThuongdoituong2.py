#Method: PHƯƠNG THỨC:
class Item():
    def __init__(self, name=str, price=float, quantity=float):
        self.name = name
        self.price = price
        self.quantity = quantity

        #KIỂM TRA ĐIỀU KIỆN THUỘC TÍNH: NẰM CHUNG TRONG PHẦN KHAI BÁO CLASS BAN ĐẦU
        assert price >= 0 #f"{price} không hợp lệ, giá phải đảm bảo > 0
        assert  quantity>=0
    # KHỞI TẠO PHƯƠNG THỨC BÌNH THƯỜNG:
    def tong_gia(self): #khai báo phương thức.

        return self.price * self.quantity #phép tính
    # KHỞI TẠO PHƯƠNG THỨC TĨNH:
    @staticmethod
    def Checkgia(gia):
        if gia<=500:
            return "Cheap, mặt hàng để ở tầng 1"
        else:
            return "Expensive, mặt hàng để ở tầng 2"
item1 = Item("Phone",1000.5,2.5)
item2 = Item("Laptop",3000,2)
item3 = Item("Tivi",5000,5)
print(item3.name)
print(f"Tổng giá trị số lượng của điện thoại là: {item1.tong_gia()}$")
print(Item.Checkgia(600))

#kHAI BÁO THUỘC TÍNH CON: ngang bằng với thuộc tính lass cha:
class Phone(Item):
    def __init__(self, name=str, price=float, quantity=float,loai="4G"): # giữ nguyên thuộc tính class cha, và thêm vào các thuộc tính con
        super().__init__(name,price,quantity)
        self.loai=loai   # khởi tạo các đối tượng con
phone1=Phone("Samsung A52",1000,5,) # nếu không nhập loai thì mặc định nó sẽ hiểu là loai ban đầu khai báo, cụ thể khai báo ở đây là 4G
phone2=Phone("Iphone 16",2000,10,"5G")
print(f"{phone1.name} là điện thoai {phone1.loai} có giá là {phone1.price}$")
print(f"{phone2.name} là điện thoai {phone2.loai} có giá là {phone2.price}$")
print(f"Tổng giá trị số lượng của điện thoại Samung A52 là: {phone1.tong_gia()}$")