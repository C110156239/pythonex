x=list(input("輸入一組四位數字為:"))
z=[]
for i in range(4):
    y=(int(x[i])+7)%10
    z.append(y)
a=z[0]
z[0]=z[2]
z[2]=a
a=z[1]
z[1]=z[3]
z[3]=a
print("輸出加密後的數字為:"+str(z[0])+str(z[1])+str(z[2])+str(z[3]))