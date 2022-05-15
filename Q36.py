x=int(input("輸入共有X筆測試資料:"))

for i in range(x):
    y=[]
    a=0
    for j in range(0,4):
        y.append(int(input()))
    if y[1]-y[0]==y[2]-y[1]==y[3]-y[2]:
        y.append(y[3]+y[3]-y[2])
        print(y,"此為等差數列")
    elif y[1]/y[0]==y[2]/y[1]==y[3]/y[2]:
        y.append(y[3]*y[2]/y[1])
        print(y,"此為等比數列")