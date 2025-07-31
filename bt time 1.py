#nhập tên và tuổi của mình để chương trình in ra năm mình 100 tuổi
import time
ten = input("Mời nhập vào tên: ")
tuoi = int(input("Mời nhập tuổi hiện tại:"))
hientai=time.localtime()
nam = hientai.tm_year
print(f"Năm bạn {ten} 100 tuổi sẽ là năm: ",nam +(100-tuoi))