


x = list(map(int,input().split(",")))
x.sort()

y=0
z=0
for i in range(0,len(x)):
    y+=x[i]*(10**i)
x.reverse()

for i in range(0,len(x)):
    y+=x[i]*(10**i)
print(y-z)
    
    


    