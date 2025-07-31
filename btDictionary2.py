#Dict 02: Cho: (check phần miêu tả video để copy dict_01 )
dict_01 = {
"A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
"H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
"V":4,"W":4,"X":8,"Y":4,"Z":10}
#1: Tách số và chữ , hiển thị lên màn hình
#2: tính tổng các số
#3: chuyển đổi chuỗi : "University of Technology and Education" sang số
print("Giai y so 1:")
lst_chu=[]
lst_so=[]
for i in dict_01:
    lst_chu.append(i)
    lst_so.append(str(dict_01[i]))
#print(lst_chu)
#print(lst_so)
print(f"Phan chu sau khi duoc tach la: {" ".join(lst_chu)}")
print(f"Phan so sau khi duoc tach la: {" ".join(lst_so)}")

print("Giai y so 2:")
tong=0
for i in dict_01:
    tong+=(dict_01[i])
print("Tong cac so se la:",tong)
print("Giai y so 3:")
a = "University of Technology and Education"
#cách 1:
print(a.split())
s="".join(a.split()) #bỏ dấu cách, nối các chữ lại với nhau
print(s)
k = ""
for j in s:
    k=k+str(dict_01[j.upper()])
print(f"Chuoi {a} sau khi chuyen doi sang so sẽ duoc ket qua là: {k}") #=>kết quả in ra các số sẽ viết liền
#cách 2:
lst_so=[]
for j in s:
    if j.upper() in dict_01:
        lst_so.append(str(dict_01[j.upper()]))
chuoi_so=" ".join(lst_so)
print(f"Chuoi {a} sau khi chuyen doi sang so se duoc ket qua là: {chuoi_so}") #=>kết quả in ra các số sẽ cách nhau 1 dấu cách
#cách 3:
noi=""
for kytu in a:
    if kytu==" ": # nếu ký tự trong chuỗi mà bằng dấu cách
        noi=noi+kytu
    else:
        noi=noi+str(dict_01[kytu.upper()]) # ép sang dạng string
        #print(noi)
print(f"Chuoi {a} sau khi chuyen doi sang so se duoc ket qua là: {noi}")
