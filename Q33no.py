chinese = int(input("國文:"))
english =int(input("英文:"))
calculus = int(input("微積分:"))
physicaleducation =int(input("體育:"))
programming = int(input("程式設計:"))

if 0<=chinese<=100 and 0<=english<=100 and 0<=calculus<=100 and 0<=physicaleducation<=100 and 0<=programming<=100:
    su = chinese + english + calculus + physicaleducation + programming
    avg = su % 5
    print(avg)