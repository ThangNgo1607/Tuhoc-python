#viết chương trình trả lời kết quả các phép tính trong danh sách sau: a=["2+5+7=","5*10=","sqrt(16)=","12%2=","5//2="]



a = ["2 + 5 + 7 =", "5 * 10 =", "sqrt(16)=", "12%2=", "5//2="]

import math
'''for pheptinh in a:
    # Loại bỏ dấu '=' ở đầu và cuối để lấy phần biểu thức(ở đây biểu thức chỉ có dấu bằng ở cuối)
    bieuthuc = pheptinh.strip("=")

    # Nếu có 'sqrt' thì dùng math.sqrt
    if 'sqrt' in bieuthuc:
        # Lấy số bên trong sqrt(...)
        so = float(bieuthuc[bieuthuc.find('(')+1 : bieuthuc.find(')')])
        ketqua = math.sqrt(so)
        Đây là dòng quan trọng. Nó đang lấy ra số nằm bên trong dấu ngoặc sqrt(...), và ép thành số thực (kiểu float).bieu_thuc.find('(')
        →Tìm vị trí dấu ngoặc mở (
        → Với "sqrt(16)", dấu ( nằm ở vị trí số 4 (tính từ 0).
        
        bieu_thuc.find(')')
        → Tìm vị trí dấu ngoặc đóng )
        → Với "sqrt(16)", dấu ) nằm ở vị trí số 7.
        
        bieu_thuc[bieu_thuc.find('(')+1 : bieu_thuc.find(')')]
        → Lấy chuỗi con nằm giữa hai dấu ngoặc: từ sau dấu ( đến trước dấu )
        → Tức là: "sqrt(16)"[5:7] → "16"
        
        float(...)
        → Ép chuỗi "16" thành số thực 16.0
    else:
        # Dùng eval để tính kết quả
        ket_qua = eval(bieuthuc)

    # In ra phép tính và kết quả
    print(f"{pheptinh} {ketqua}")'''
for pheptinh in a:
    bieuthuc = pheptinh.strip("=")
    if "sqrt" in bieuthuc:
        so = float(bieuthuc[bieuthuc.find("(")+1:bieuthuc.find(")")])
        ketqua=math.sqrt(so)
    else:
        ketqua=eval(bieuthuc)
    print(f"{pheptinh} {ketqua}")
print("-"*20)


#có thể sử dụng sqrt hiệu quả hơn bằng cách như sau:
from math import sqrt
for pheptinh in a:
    bieuthuc = pheptinh.strip("=")
    ketqua=eval(bieuthuc)
    print(f"{pheptinh} {ketqua}")