d = int(input("請輸入一個度數:"))
if (d <= 120 and d >= 0):
    print("Summer months:", d*2.10)  
    print("Non-Summer months", d*2.10)
elif (d >= 121 and d <= 330):
    print("Summer months:", d*3.02)
    print("Non-Summer months", d*2.68)
elif (d >= 331 and d <= 500):
    print("Summer months:", d*4.39)
    print("Non-Summer months", d*3.61)
elif (d >= 501 and d <= 700):
    print("Summer months:", d*4.97)
    print("Non-Summer months", d*4.01)
else :
    print("Summer months:", d*5.63)
    print("Non-Summer months", d*4.50)
