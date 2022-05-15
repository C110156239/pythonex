a=int(input())
for i in range(a):
    b=int(input())
    if b%9==0 or b%11==0:
        print("第",i+1,"個點:",b)
        continue
    