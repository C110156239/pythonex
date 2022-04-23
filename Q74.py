ans = ["red","blue","red","green"]

for i in range(10):
    a = input("輸入顏色:").split(" ")
    b = ""
    for j in range(0,len(a)):
        if a[j] == ans[j]:
            b = b + "1"
        elif a[j] in ans:
            b = b + "2"
        else:
            b = b + "3"

    if b == "1111":
        print("正確答案")
        break

    if i == 9:
        print("挑戰失敗")
        break

    print(b)
