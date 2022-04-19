m = int(input("輸入月份:"))
d = int(input("輸入日期:"))
s = (m*2|d)%3
if s == 0:
    print("運勢普通")
elif s == 1:
    print("運勢吉")
elif s == 2:
    print("運勢大吉")
