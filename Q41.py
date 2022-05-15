x=int(input("搭了幾次電梯:"))
a=0
y=[]
for i in range(x):
    y.append(input())

a=(int(y[0])-1)*20
for i in range(len(y)):
    if i>=1:
        if  int(y[i])>int(y[i-1]):
            a=a+(int(y[i])-(int(y[i-1])))*20
        elif int(y[i])<int(y[i-1]):
            a=a+(int(y[i-1])-int(y[i]))*10
print(a,"元")