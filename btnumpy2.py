#Tạo một ma trận numpy 8*8, có thứ tự ma trận các dòng từ 1-7 là: 01010101, dòng thứ 8 ngược lại là 10101010
import numpy as np
a=np.zeros((8,8))
print(a)
for collum in range(a.shape[1]):
    #print(collum)
    if collum%2!=0:
        a[0:7,collum]=1 # a tại dòng từ index 0 đến 6 và cột collum số lẻ
        #print(collum)
        #print(a)
    else:
        a[-1,collum]=1 ## a tại dòng cuối cùng và cột collum số chẵn
print(a)