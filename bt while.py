while True:
    hoten = input("Mời nhập vào tên: ")
    monhoc = input("Mời nhập vào mô học: ")
    diemthi = float(input("Mời nhập vào điểm thi: "))
    print(f"Học sinh {hoten} dự thi môn {monhoc} có số điểm {diemthi}")
    if diemthi>=7:
        print("Xếp loại điểm : ĐẠT")
    else:
        print("Xếp loại điểm: KHÔNG ĐẠT")
    a = input("Nhập n để thoat hoặc nhấn phím bất kỳ để tiếp tục:")
    if a=='n' or a=='N':
        break

