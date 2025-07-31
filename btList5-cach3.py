s = [2, 12, 3, 3, 7, 2, 5, 7, 2, 6]
lst = sorted(s)
print(lst)
max_2 = []

# Tìm số lớn thứ 2 (khác lớn nhất)
for i in range(len(lst) - 2, -1, -1):  # duyệt ngược từ phần tử áp chót về đầu
    if lst[i] < lst[-1]:  # nếu nhỏ hơn max => chính là lớn thứ 2
        second_max = lst[i]
        break

# Tìm vị trí của nó trong list gốc
for j in range(len(s)):
    if s[j] == second_max:
        max_2.append(j)

print(f"Số lớn thứ 2 là: {second_max}, vị trí index trong list là: {max_2}")