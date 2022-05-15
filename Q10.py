while True:
    
        a, b = input("輸入 N 及 M 為:").split(" ")
        if a=="0" and b=="0":
            break
        a = int(a)
        b = int(b)
        array = []
        for i in range(a):
            array.append(input("輸入矩陣數值第{}列數值為 : ".format(i+1)).split(" "))
        for i in range(b):
            for j in range(a):
                print(int(array[j][i]), end = ' ')
            print('')