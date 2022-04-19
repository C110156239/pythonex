import math

a = int(input("輸入a值:"))
b = int(input("輸入b值:"))
c = int(input("輸入c值:"))

k = b**2-4*a*c #b平方-4ac
if k>0:
        x1=(-b+math.sqrt(k))/2*a
        x2=(-b-math.sqrt(k))/2*a
        print("有兩解",(x1,x2))
if k==0:
        x1=-b/2*a
        x2=x1
        print("為唯一解",x1)
if k<0:
        print("為無解",'0')
