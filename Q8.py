while True:
    tr = input("請輸入要檢測的字串(end結束):")
    print("要檢測的字串:",tr)

    if tr == "end":
        print("檢測結束")
        break

    yu = input("請輸入要檢測單一的字元(end結束):")
    if yu == "end":
        print("檢測結束")
        break

    co = tr.count(yu)
    print("字元",yu,"出現次數為",co)