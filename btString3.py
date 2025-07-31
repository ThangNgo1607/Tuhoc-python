#viết chương trình in ra vị trí của ký tự a trong chuỗi "hom nay troi dem qua, chung minh di choi thoi nao"

vidu = "hom nay troi dep qua, chung minh di choi thoi nao"
print(f"độ dài của vidu là {len(vidu)} ký tự")
a2 = ""
for i in range(len(vidu)):
    #print(i)
    if vidu[i]=="a": 
        a2 = a2+" "+str(i)
        print(a2)
print(f"vị trí của ký tự a trong chuỗi là: {a2}")
