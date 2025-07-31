# cho mảng sau L= [[1,4,3,7],[2,0,1,8],[4,6,2,4],[7,3,8,3],[2,5,3,1]]. Định nghĩa 1 hàm để đổi ma trận từ dạng(a dòng b cột) 
# thành ( b dòng a cột)
L= [[1,4,3,7],[2,0,1,8],[4,6,2,4],[7,3,8,3],[2,5,3,1]]
import numpy as np
a=np.array(L)
print(a)
b=a.T   #.T là thuộc tính của NumPy array, viết tắt của Transpose. hoán đổi hàng thành cột, cột thành hàng.
print(b)