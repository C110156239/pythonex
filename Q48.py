x=int(input("輸入整數n:"))
z=[]
for i in range(x):
    z.append(input().split())
s=input("輸入欲查詢單字")
for i in range(len(z)):
    if s==z[i][0]:
        print(z[i][0],"中文意思為:",z[i][1])