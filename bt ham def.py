# bài toán đầu tư hoặc không đầu tư
def roi(cp,dt):
    if (dt-cp)/cp>=0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
cp = float(input("Mời nhập vào chi phí: "))
dt = float(input("Mời nhập vào doanh thu: "))
a = roi(cp,dt)
print(a)
print(f"Vì tỷ lệ ROI = {round((dt-cp)/cp,2)}")
