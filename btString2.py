vidu6 = "le dinh tu;pham thi ghi;pham thi bap"
o = vidu6.split(";")
print(f"kết quả của o là: {o}") #=> kết quả là xuất ra dạng list: ['le dinh tu','pham thi ghi','pham thi bap']
for i in o:
    print(i)
o1 =",".join(o) # CÚ PHÁP NỐI CÁC PHẦN TỬ TRONG MẢNG LẠI VỚI NHAU THÀNH CHUỖI,(muốn nối kỹ tự gì thì đưa ký tự đó vào .join(thêm mảng đó vào))
print(o1) # => kết quả là: le dinh tu,pham thi ghi,pham thi bap