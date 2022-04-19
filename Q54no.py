km = float(input("請輸入路程公里數(km):"))
me = km*1000
if km <=1.5:
    print("所需車資為:75")
elif me > 1500 and me >= 1750:
    if (me-1500)%250 != 0:
        print("所需車資為:",75+(((me-1500)/250)*5)+1)
    elif (me-1500)%250 == 0:
        print("所需車資為:",75+(((me-1500)/250)*5))
elif me > 1500 and me < 1750:
    print("所需車資為:80")
