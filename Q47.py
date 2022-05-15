x=int(input("輸入比數n:"))
z=["金","銀","銅","優"]
y=[]
for i in range(x):
    a=int(input("{}".format(z[i])))
    y.append(a)


print("金牌得到{}面".format(y[0]))
print("銀牌得到{}面".format(y[1]))
print("銅牌得到{}面".format(y[2]))
print("優牌得到{}面".format(y[3]))