Number = int(input("請輸入正整數n :"))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print("Perfect Number")
elif Sum > 12:
    print("Abuadant Number")
elif Sum < 9:
    print("Defieient Number")