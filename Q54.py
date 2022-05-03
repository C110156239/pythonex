km = float(input("請輸入路程公里數(km):"))
a = 75
if km <= 1.5:
    print("所需車資為:",a)
elif km > 1.5:
    if km-1.5 < 0.25:
        print("所需車資為:",a+5)

    elif (km-1.5)%0.25 != 0:
        b=(km-1.5)//0.25+1
        a=a+b*5
        print("所需車資為:",a)

    else:
        b=(km-1.5)//0.25
        a=a+b*5
        print("所需車資為:",a)
