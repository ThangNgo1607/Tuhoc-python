'''from random import randrange
a=randrange(1,100)
print(a)
guess=int(input("Xin mời bạn đoán số từ 1-100 : "))
dem=1
while guess!=a:
    dem+=1
    if guess > a:
        print(guess,"số bạn đoán cao quá, vui lòng thử lại.")
    if guess < a:
        print(guess, "số bạn đoán thấp quá, vui lòng thử lại.")
    guess = int(input("Xin mời đoán lại số: "))
    if dem==5:
        print("Bạn đã hết lượt đoán")
        break
if guess==a:
    print(guess, "là số may mắn của chương trình, chúc mừng bạn đã chiến thắng")'''

# cách 2
from random import randrange
rs = randrange(1,100)
print(rs)
count = 1 #(có thể để count = 4)
guess = int(input("Bạn hãy đoán số của mình: "))
while True:
    if guess == rs:
        print("Chúc mừng bạn đã đoán đúng số may mắn là {}".format(rs))
        break
    elif guess < rs:
        count += 1 #(count-=1)
        print("Thật tiếc! Số bạn đoán nhỏ hơn số may mắn rồi")
        guess = int(input("Bạn hãy đoán lại số của mình: "))
        if count == 5:#(count-=1)
            print("Chúc bạn may mắn lần sau!")
            break
    elif guess > rs:
        count += 1
        print("Thật tiếc! Số bạn đoán lớn hơn số may mắn rồi")
        guess = int(input("Bạn hãy đoán lại số của mình: "))
        if count == 5:
            print("Chúc bạn may mắn lần sau!")
            break