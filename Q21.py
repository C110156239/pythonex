form1 = {"123":"123 Tom DTGD","456":"456 Cat CSIE","789":"789 Nana CSIE","321":"321 Lim DBA","654":"654 Won FDD"}
number = input("輸入查詢學號:")

student = form1.get(number)
if student == None:
    print("查無此學生")
else:
    print("學生資料為:"+(form1[number]))
