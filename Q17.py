xx=[]
yy=[]
zz=[]
aa=[]
a=0
b=0
z=0
x1=input().split()
x2=xx.append(input().split(" "))
x3=xx.append(input().split(" "))
y1=input().split()
y2=yy.append(input().split(" "))
y3=yy.append(input().split(" "))

if int(x1[0])==int(y1[0]) and int(x1[1])==int(y1[1]):
    if len(xx)==len(yy) and len(xx[0]) == len(yy[0]):
        for i in range(len(xx)):
            aa=[]
            for j in range(len(xx[0])):
                z=0
                z=int(xx[i][j])+int(yy[i][j])
                aa.append(z)
                zz.append(aa)
        
        print(zz[0])
        print(zz[-1])
else:
    print("兩個矩陣無法相加")
        
