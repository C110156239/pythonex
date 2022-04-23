M = int(input('請輸入階層值M？'))
fac = 1
i = 1
while(fac < M):
        i = i + 1
        fac = fac * i
print("超過M為1000的最小階層N值為:",i)