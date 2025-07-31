# cho mảng sau L= [[1,4,3,7],[2,0,1,8],[4,6,2,4],[7,3,8,3],[2,5,3,1]]. Định nghĩa 1 hàm để đổi ma trận từ dạng(a dòng b cột) 
# thành ( b dòng a cột)
L= [[1,4,3,7],[2,0,1,8],[4,6,2,4],[7,3,8,3],[2,5,3,1]]
import numpy as np
def chuyendoimatran(L):
    a=np.array(L)
    #print(a)
    b=np.zeros((a.shape[1],a.shape[0])) # tạo thêm một MT tòn số 0
    #print(b)
    dem=0
    for i in a: #duyệt các dòng trong a
        #print(i)
        b[:,dem]=i # thay đổi các cột của b thành dòng của a
        dem+=1
    return b
print(chuyendoimatran(L))



import numpy as np
lst = [[1,4,3,7],[2,0,1,8]]
arr = np.array(lst)
print(arr)
arr1 = np.zeros((arr.shape[1],arr.shape[0])) # tạo thêm một MT tòan số 0

for i in range(arr.shape[1]):
    for j in range(arr.shape[0]):
        arr1[i,j] = arr[j,i]

print(arr1)