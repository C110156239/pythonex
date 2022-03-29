x = int(input("請輸入一個度數:"))

if (x <= 120 ):
    print("Summer months:"+"%6.2f"%(x*2.1)+"元")  
    print("Non-Summer months"+"%6.2f"%(x*2.1)+"元")
elif 120< x <= 330:
    print("Summer months:"+"%6.2f"%(120*2.1 + (x-120)*3.02)+"元")  
    print("Non-Summer months"+"%6.2f"%(120*2.1 + (x-120)*2.68)+"元")
elif 330 < x <= 500:
    print("Summer months:"+"%6.2f"%(120*2.1 + 210*3.02 + (x-330)*4.39)+"元")  
    print("Non-Summer months"+"%6.2f"%(120*2.1 + 210*2.68 + (x-330)*3.61)+"元")
elif 500 < x <= 700:
    print("Summer months:"+"%6.2f"%(120*2.1 + 210*3.02 + 170*4.39 + (x-500)*4.97)+"元")  
    print("Non-Summer months"+"%6.2f"%(120*2.1 + 210*2.68 + 170*3.61 + (x-500)*4.01)+"元")
elif 700 < x:
    print("Summer months:"+"%6.2f"%(120*2.1 + 210*3.02 + 170*4.39 + 200*4.97 + (x-700)*5.63)+"元")  
    print("Non-Summer months"+"%6.2f"%(120*2.1 + 210*2.68 + 170*3.61 + 200*4.01 +(x-500)*4.5)+"元")