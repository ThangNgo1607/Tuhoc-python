#cho mảng sau [[34,43,73],[82,22,12],[53,94,66]], hoám đổi vị trí cột số 0 và cột số 2 trong mảng,
# tương tự hoán đổi vị trí dòng số 0 và dòng số 1 trong mảng
arr=[[34,43,73],[82,22,12],[53,94,66]]
import numpy as np
a=np.array(arr)
print(a)
print("hoán đổi chổ cho cột index 0 và index 2:")
'''for i in a:
    i[0],i[2]=i[2],i[0] # dòng i tại index 0 sẽ đổi thành dòng i tại idex 2, dòng i tại index 2 sẽ đổi thành dòng i tại idex 0
print(a)'''
for i in range(a.shape[0]):   # a.shape[0] là số dòng
    # Lấy ra từng phần tử cụ thể rồi gán lại
    temp = a[i,0]
    a[i,0] = a[i,2]
    a[i,2] = temp # cụ thế i sẽ chạy từ index 0: temp = dòng a[0,0] sau đó gán a[0,0]=a[0,2] sau đó lại gán lại a[0,2]=temp tức là a[0,0]
                    #tương tự các index 1,2 cũng sẽ chạy như vậy
print(a)

print("hoán đổi vị trí dòng số 0 và dòng số 1 trong mảng:")
b=np.array(arr)
print(b)
b[0],b[1]=b[1].copy(),b[0].copy() # viết ngắn gọn hơn: b[[0,1]]=b[[1,0]]
print(b)