#cho list cụ thể: s = [2, 12, 3, 7, 2, 5, 7, 2, 6], tìm sô nhỏ thứ 2 và lớn thứ 2 trong list

## Tìm số nhỏ thứ 2 (khác số nhỏ nhất)
s = [2, 12, 3, 3, 7, 2, 5, 7, 2, 6]
print(s)
lst = sorted(s)         # sắp xếp số trong list tăng dần
lst1 = sorted(s,reverse=True)       # Sắp xếp số trong list giảm dần
print(lst)
print(lst1)
for i in range(len(lst) - 1):  # Giới hạn chỉ tới phần tử áp chót, để tránh khi lst[i] tới phần tử cuối cùng sẽ 
                                #k bị lỗi khi so sánh với lst[i+1]
    if lst[i] < lst[i + 1]:
        second_min = lst[i + 1] # secon_min là số nhỏ thứ 2
        break
for i in range(len(lst1) - 1):    # Giới hạn chỉ tới phần tử áp chót, để tránh khi lst[i] tới phần tử cuối cùng sẽ  
    if lst1[i]>lst1[i+1]: 
        second_max = lst1[i+1]  # secon_max là số lớn thứ 2
        break
# Tìm vị trí của second_min và secon_max trong list gốc
min_2=[]
max_2=[]
for j in range(len(s)):
	if s[j]==second_min:
		min_2.append(j)
for j in range(len(s)):
    if s[j]==second_max:
        max_2.append(j)           
#đoạn này có thể viết gọn lại như sau: min_2 = [j for j in range(len(s)) if s[j] == second_min]
print(f"Số nhỏ thứ 2 là: {second_min}, vị trí index trong list là: {min_2}")
print(f"Số lớn thứ 2 là: {second_max}, vị trí index trong list là: {max_2}")