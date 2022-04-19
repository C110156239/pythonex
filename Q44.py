count = int(input("輸入班級個數:"))
a = 1
while a <= count:
    m = int(input("請輸入第{}個班級的人數".format(a)))
    if a == 1:
        max = min = m
    else:
        if m < min:
            min = m
        elif m > max:
            max = m
    a += 1
print("須購買的電腦數量為:",max)
