x=int(input("輸入查詢組數N為:"))

for i in range(x):
    y=input().split()
    if y[0]=="123" and y[1]=="456":
        print(9000)
        continue
    elif y[0]=="456"and y[1]=="789":
        print(5000)
        continue
    elif y[0]=="789"and y[1]=="888":
        print(6000)
        continue
    elif y[0]=="336"and y[1]=="558":
        print(10000)
        continue
    elif y[0]=="775"and y[1]=="666":
        print(12000)
        continue
    elif y[0]=="566"and y[1]=="221":
        print(7000)
        continue
    else:
        print("error")
        continue
