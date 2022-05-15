x=input("輸入一整數序列為:").split(" ")
y=0
z=0
a=0
b=0
for i in range(len(x)):
    z=0
    for j in range(len(x)):
        if x[i] == x[j]:
            z=z+1  
            if z>b:
                a=x[i]
                b=z
if b>1:
    print("過半元素為:",a)
else:
    print("過半元素為:NO")