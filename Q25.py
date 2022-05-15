a=input("請輸入考試次數及學生數:").split(" ")
b=input("每次考試所佔的比例:").split(" ")
sum=0

for i in range(int(a[1])):
    z=input().split()
    for j in range(int(a[0])):
        sum+=int(z[j])*float(b[j])
print("{:.2f}".format(sum/3))