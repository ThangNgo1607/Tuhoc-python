"""for i in range(10,51,1):
    if i%3==0:
        print(i,end=" ")"""

#cách 2
for i in range(10,51,1):
    if i%3!=0:
        continue
    print(i,end=" ")
print()
    

for i in range(0,51,1):
    if i%3==0 and i<40:
        print(i,end=" ")
   