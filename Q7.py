types = int(input("輸入月租費形式:")) 
time = int(input("輸入通話時間(second):"))
if types == 186:
    if time*0.09 < 186:
        print("通話費為186元")
    elif time*0.09 > 186 and time*0.09 <=372:
        print("通話費為",(time*0.09)*0.9,"元")
    elif time*0.09 > 372 :
        print("通話費為",(time*0.09)*0.8,"元")
elif types == 386:
    if time*0.08 < 386:
        print("通話費為386元")
    elif time*0.08 > 386 and time*0.08 <=772:
        print("通話費為",round((time*0.08)*0.8),"元")
    elif time*0.08 > 772 :
        print("通話費為",round((time*0.08)*0.7),"元")
elif types == 586:
    if time*0.07 < 586:
        print("通話費為586元")
    elif time*0.07 > 586 and time*0.07 <=1172:
        print("通話費為",round((time*0.07)*0.7),"元")
    elif time*0.07 > 1172 :
        print("通話費為",round((time*0.07)*0.6),"元")
elif types == 986:
    if time*0.06 < 986:
        print("通話費為986元")
    elif time*0.06 > 986 and time*0.06 <=1972:
        print("通話費為",round((time*0.06)*0.6),"元")
    elif time*0.06 > 1972 :
        print("通話費為",round((time*0.06)*0.5),"元")
