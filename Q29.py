x=list(input("甲方的數字:"))
y=list(input("乙方的數字:"))
for i in range(len(x)):
    if int(x[i])==1 and int(y[i])==5:
        print("贏",end="")
    elif int(x[i])==5 and int(y[i])==1:
        print("輸",end="")
    elif int(x[i])==int(y[i])+1:
        print("贏",end="")
    elif int(y[i])==int(x[i])+1:
        print("輸",end="")
    else:
        print("和",end="")