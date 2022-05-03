a=[]
chinese = a.append(int(input("國文:")))
english = a.append(int(input("英文:")))
calculus = a.append(int(input("微積分:")))
physicaleducation = a.append(int(input("體育:")))
programming = a.append(int(input("程式設計:")))

b=0

for i in range(len(a)):
    b=b+a[i]
print("平均分數:{:.2f}".format(b/len(a)))
a.sort()
print("最高分科目:",a[-1],"分")
print("最低分科目:",a[0],"分")