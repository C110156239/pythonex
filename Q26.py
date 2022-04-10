while True:
    tr = input("檢測的字串(end結束):")
    

    if tr == "end":
        print("檢測結束")
        break

    yu = input("檢測的單一字元:")
    
    co = tr.count(yu)
    print("字元",yu,"出現次數為",co)

    