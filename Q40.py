from re import A


a=int(input("輸入整數n:"))

for i in range(1,a,2):
    print((a-(a//3*2))*" ",i,end="")
    print("")
for i in range(1,a+2,2):
    print(i,end="")
for i in range(a-2,-1,-2):
    print(i,end="")
print("")
for i in range(a-2,-1,-2):
    print((a-(a//3*2))*" ",i,end="")   
    print("")