x=int(input("輸入比數n:"))
y={"金":0,"銀":0,"銅":0,"優":0}
z=list(y)

for i in range(x):
    a=int(input("{}".format(z[i])))
    y[z[i]]=a


print("金牌得到{}面".format(y["金"]))
print("銀牌得到{}面".format(y["銀"]))
print("銅牌得到{}面".format(y["銅"]))
print("優牌得到{}面".format(y["優"]))
