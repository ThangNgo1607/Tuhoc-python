#from math import sqrt
print("Giải phương trình bậc 2: ax^2 + bx +c =0")
a = float(input("Mời nhập vào giá trị của a: "))
b = float(input("Mời nhập vào giá trị của b: "))
c = float(input("Mời nhập vào giá trị của c: "))
delta = b**2-4*a*c
if delta<0:
    print("phương trình bậc hai vô nghiệm")
elif delta==0:
    print(f"phương trình bậc 2 có nhiệm kép: x1 = x2 = {-b/2*a}")
else:
    from math import sqrt
    print("phương trình bậc hai có 2 nghiệm phân biệt:")
    print(f"x1 = {(-b+sqrt(delta))/(2*a)}")
    print(f"x2 = {(-b-sqrt(delta))/(2*a)}")