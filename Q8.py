x=int(input("輸入第一行正整數:"))
y=input("輸入第二行中數列中的數字為:").split(" ")
z = 0
a = 0
b = 0
for i in range(len(y)):
      z=0
      for j in range(len(y)):
            if  y[i] == y[j]:
                  z=z+1
                  if z>b:
                        a=y[i]
                        b=z
if a!=0 and b!=0:
      print("最大出現次數的數字為:",a,"  出現次數為:",b)
else:
      print("每個數字剛好只出現1次")






