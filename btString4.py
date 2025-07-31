# cho a = "chung tA cua tuong lAi".hãy viết một đoạn code để đếm được trong chỗi "a" có bao nhiêu nguyên âm.
a = "chung tA cua tuong lAi"
#cho chỗi a trở thành chuỗi viết liền nhau
b = "".join(a.split())
# Danh sách các nguyên âm không dấu:
nguyen_am = "ueoai"

# Đếm số lượng nguyên âm trong chuỗi
demnguyenam = 0
demphuam = 0
for char in b:
    #print(char)
    if char.lower() in nguyen_am:
        demnguyenam += 1
    if char.lower() not in nguyen_am:
        demphuam += 1


print("Số lượng nguyên âm trong chuỗi là:", demnguyenam)
print("Số lượng phụ âm trong chuỗi là:", demphuam)


#cách 2
s = input("Nhập vào một chuỗi: ")            # Yêu cầu người dùng nhập chuỗi
def demnguyenam(s):
    nguyenam = "ueoai"  # Danh sách các nguyên âm
    dem = 0                 # Biến đếm số lượng nguyên âm
    for char in s:         # Duyệt từng ký tự trong chuỗi s
        if char.lower() in nguyenam: # Nếu ký tự là nguyên ( ký tự trong chuỗi s là nguyên âm thì:)
            dem += 1     # Tăng biến đếm lên 1
    return dem           # Trả về tổng số nguyên âm'''
slnguyenam = demnguyenam(s)
def demphuam(s):
    nguyenam = "ueoai"  # Danh sách các nguyên âm
    demphuam = 0 
    n=s.replace(" ","")               
    for char in n:         # Duyệt từng ký tự trong chuỗi n
        if char.lower() not in nguyenam: # Nếu ký tự không phải là nguyên ( ký tự trong chuỗi s là phụ âm thì:)
            demphuam += 1     # Tăng biến đếm lên 1
    return demphuam           # Trả về tổng số nguyên âm'''
slphuam = demphuam(s)                 # Gọi hàm demnguyenam để đếm nguyên âm
print("Số lượng nguyên âm trong chuỗi là:", slnguyenam)  # In kết quả
print("Số lượng phụ âm trong chuỗi là:", slphuam)  # In kết quả