
#mở rộng cho người dùng nhập đáp an của phép tính để kiểm tra đáp án đúng hay sai

#cách 1:
from math import sqrt
a = ["2 + 5 + 7 = ", "5 * 10 = ", "sqrt(16) = ", "12 % 2 = ", "5//2 = "]

# for pheptinh in a:
#     bieuthuc = pheptinh.strip("= ")
#     ketqua = eval(bieuthuc)
#     dap_an = float(input(pheptinh)) # In phép tính trong input() → input(pheptinh)(cách này khó có thể in chữ)
#     if dap_an == ketqua:
#         print("✅ Đúng rồi!")
#     else:
#         print(f"❌ Sai. Đáp án đúng là: {ketqua}")
# print("-"*20)

#cách 2:
for pheptinh in a:
    bieuthuc = pheptinh.strip("= ")
    ketqua = eval(bieuthuc)
    print(f"Phép tính: {pheptinh}",end="") # In phép tính bằng print() riêng → print(f"Phép tính: {pheptinh}", end=" ") 
    #Dễ mở rộng về sau như: thêm điểm số, số lần trả lời sai, đếm câu đúng, v.v.
    dap_an = float(input())
    if dap_an==ketqua:
        print("✅ Đúng rồi!")
    else:
        print(f"❌ Sai. Đáp án đúng là: {ketqua}")