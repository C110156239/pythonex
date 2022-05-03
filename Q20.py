group = int(input("組數為:"))
for i in range (1, group+1):
    a = 0
    b = input("第{}組為:".format(i)).split()
    a = int(b[0])*250+int(b[1])*175
    print("第{}組應收費用:".format(i),a)

