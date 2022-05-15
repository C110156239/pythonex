x=input("輸入矩陣的維度:").split(" ")
y=[]
z=[]
a=[]
for i in range(int(x[0])):
    y.append(input().split())
for i in range(int(x[0])):
    z.append(input().split())
for i in range(int(x[0])):
    for j in range(int(x[1])):
        a.append(int(y[i][j])*int(z[i][j]))
for i in range(int(x[1])):
    print(a[i],end=" ")
print()
for i in range(len(a)-int(x[1]),len(a)):
    print(a[i],end=" ")