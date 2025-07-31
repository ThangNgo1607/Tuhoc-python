# cho mảng sau L= [[1,4,3,7],[2,0,1,8],[4,6,2,4],[7,3,8,3],[2,5,3,1]]. Định nghĩa 1 hàm để đổi ma trận từ dạng(a dòng b cột) 
# thành ( b dòng a cột)
L= [[1,4,3,7],[2,0,1,8],[4,6,2,4],[7,3,8,3],[2,5,3,1]]
import numpy as np
def doimatran(L):
    a=np.array(L)
    print(a)
    new=[]
    for i in range(a.shape[1]): # duyệt i chạy trong index của cột a( từ 0-3)
        new.append(a[:,i].tolist()) # chuyển thành các dòng( lấy toàn bộ dòng của a và cột i, i chạy từ o đến 3) add và mảng new
        #print(new)
        b=np.array(new)
    return b

print(doimatran(L))
