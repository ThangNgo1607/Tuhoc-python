# Tìm giá trị max và min trong array sau: [[34,43,73],[82,22,12],[53,94,66]]. sau đó xuất ra vị trí index của các số đó
arr=[[34,12,73],[82,22,12],[53,94,66]]
import numpy as np
a=np.array(arr)
print(a)
max=a[0,0]
max_index=(0,0)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j]>max:
            max=a[i,j]
            max_index=(i,j)
print("Số lớn nhất trong mảng là: ",max)
print(f"Vị trí index của số {max} là: {max_index}")
min=a[0,0]
min_index=(0,0)
lst_min=[]
for k in range(a.shape[0]):
    for h in range(a.shape[1]):
        if a[k,h]<min:
            min=a[k,h]
            min_index=(k,h)
            lst_min.append(min_index)
print("Số nhỏ nhất trong mảng là: ",min)
print(f"Vị trí index của số {min} là: {lst_min}")