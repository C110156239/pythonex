x=int(input("輸入n值:"))
y=[]
z=[]
b={}
for i in range(x):
    y.append(input("請輸入姓名:"))
    z.append(input("請輸入電子郵件:"))
for i in range(len(y)):
    b[y[i]]=z[i]
a=input("請輸入要查詢的姓名:")
print("電子郵件帳號為:",b[a])