
x = int(input("小明身上有幾元:"))
y = int(input("販賣機有幾種有料:"))        #输入二维数组的行数和列数
a=0
for i in range(y):
      z = int(input())       #输入二维数组，同行数字用空格分隔，不同行则用回车换行 
      if x>=z:
            a+=1
      print("小名可以買",a,"種飲料")      