mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu",
"Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi",
"Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi",
"Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu",
"Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi",
"Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
#Viết chương trình cho người dùng lựa trọn để tìm kiếm sách

x=False
while x==False:
    lua_chon=input("""Cho các tiêu đề:
                    1. Tên Sách (Title)
                    2. Tên Tác Giả (Author)
                    3. Nhà Xuất Bản (Publisher)
    Lựa chọn 1 hoặc 2 hoặc 3 để tìm kiếm trong thư viện: """)
    if lua_chon=="1":
        key="Title"
        break
    if lua_chon=="2":
        key="Author"
        break
    if lua_chon=="3":
        key="Publisher"
        break
    else:
        print("Bạn chọn chưa đúng số tiêu đề, mời lựa chọn lại( 1 or 2 or 3)")
        x=False 

y=False
while y==False:
    tu_khoa=input(f"Mời nhập {key} cần tìm kiếm: ")
    print("Các sách bạn tìm kiếm từ thư viện là: ")
    tim_thay=False
    for dong in mybooks:    
        if tu_khoa==dong[key]:
            print(f"Tên Sách: ",dong["Title"])
            print(f"Tác Giả: ",dong["Author"])
            print(f"NXB: ",dong["Publisher"])
            print(f"Giá: ",dong["Price"])
            print(f"Năm xuất bản: ",dong["Published_Year"])
            print("="*50)
            tim_thay=True
    if tim_thay:
        y = True  # Thoát khỏi vòng lặp while
    else:
        print("Từ khóa bạn nhập không tìm thấy trong thư viện. Vui lòng nhập lại.")
        y==False
    
              

