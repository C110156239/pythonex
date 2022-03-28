month = int(input("請輸入月份"))
date = int(input("請輸入日期"))

def get_sign(month, date):
    dateo = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    sign = ("摩羯座apricorn", "水瓶座Aquarius", "雙魚座Pisces", "牡羊座Aries", "金牛座Taurus", "雙子座Gemini", "巨蟹座Cancer", "獅子座Leo", "處女座Virgo", "天秤座Libra", "天蝎座Scorpio", "射手座Sagittarius")
    if date < dateo[month-1]:
        return sign[month-1]
    else:
        return sign[month]

print ("星座為:",(get_sign(month,date)))

