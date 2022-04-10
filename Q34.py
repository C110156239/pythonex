new = int(input("輸入一正整數:"))
if new>=11 and new<=1000:
    if new%2 == 0 and new%11 ==0 and new%5 != 0 and new%5 != 0:
        print(new,"為新公倍數?:","YES")
    else:
        print(new,"為新公倍數?:","NO")