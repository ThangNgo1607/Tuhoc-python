#Dict 03: Cho data 1 cửa hàng, dữ liệu kiểu như sau : (check phần miêu tả video để copy mybook )
d=[
{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
{"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
{"name":"Trung","phone":"555-3141","email":""},
{"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]
#1. Tìm tất cả user có số điện thoại kết thúc bằng 8
#2: tìm tất cả user o có địa chỉ email
print("1.Các user có số điện thoại kết thúc bằng 8 là: ")
for dong in d:
    #print(dong) d thuộc dạng List, sau khi duyệt dong sẽ thành dạng Dictionary
    #print(dong["phone"]) #tìm key của phone sẽ ra value sđt thuộc dạng string
    #print(dong["phone"][-1]) tìm ký tụ cuối cùng của chuỗi string
    if dong["phone"][-1] == "8": #"8" 8 sỏ đây đang dạng chuỗi ký tự chứ k phải dạng số nên phải nằm trong nháy kép
        print("*"*50)
        print("Name= ",dong["name"])
        print("Phone= ",dong["phone"])
        print("Email= ",dong["email"])
print("_"*50)
print("2: Tất cả user không có địa chỉ email là: ")
for dong in d:
    if dong["email"] == "":
        print("Name= ",dong["name"])
        print("Phone= ",dong["phone"])
        print("Email= ",dong["email"])
