#cho mảng sau [[34,43,73],[82,22,12],[53,94,66]], hoám đổi vị trí cột số 0 và cột số 2 trong mảng,
# tương tự hoán đổi vị trí dòng số 0 và dòng số 1 trong mảng
arr=[[34,43,73],[82,22,12],[53,94,66]]

print("hoán đổi chổ cho cột index 0 và index 2:")
import numpy as np
a=np.array(arr)
print(a)
a_change = tuple(a[:,0].tolist())   #tuple(int(x) for x in a[:,0]), nếu k gán tuple thì a_change sẽ thay đổi theo a ở dưới
print(a_change)
a[:,0]=a[:,2]
#print(a)
a[:,2]=a_change
print(a)

print("hoán đổi vị trí dòng số 0 và dòng số 1 trong mảng:")
b=np.array(arr)
b_change=tuple(b[0,:].tolist()) #b[0]
print(b_change)
b[0,:]=b[1,:] #b[1]
b[1,:]=b_change
print(b)