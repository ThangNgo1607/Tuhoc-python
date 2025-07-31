# Tìm giá trị max và min trong array sau: [[94,43,73],[82,22,12],[12,94,66]]. sau đó xuất ra vị trí index của các số đó
L=[[94,43,73],[82,22,12],[12,94,66]]
import numpy as np
a=np.array(L)
print(a)
#tìm max và min của a:
max_a=np.max(a) #duyệt qua tất cả các phần tử trong mảng 2 chiều và trả về phần tử lớn nhất. thay vì gõ chi tiết qua vòng lặp for
min_a=np.min(a) #duyệt qua tất cả các phần tử trong mảng 2 chiều và trả về phần tử nhỏ nhất. thay vì gõ chi tiết qua vòng lặp for

#tìm vị trí của số lớn nhất và số nhỏ nhất
max_aindex=[]   #tạo list rỗng
min_aindex=[]
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j]==max_a:
            max_aindex.append((i,j))
        if a[i,j]==min_a:
            min_aindex.append((i,j))
print(f"số lớn nhất trong mảng là: {max_a}, xuất hiện ở vị trí index: {max_aindex}")
print(f"số nhỏ nhất trong mảng là: {min_a}, xuất hiện ở vị trí index: {min_aindex}")