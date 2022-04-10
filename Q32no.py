# dollar = input("小名身上有幾元:")
# several = input("販賣機有幾種有料:")
# for i in range(several):


dollar = input("小明身上有幾元:")
n = int(input("販賣機有幾種有料:"))        #输入二维数组的行数和列数

for i in range(n):
      m = input().split(" ")       #输入二维数组，同行数字用空格分隔，不同行则用回车换行 
if m <= dollar:
    print(n)      