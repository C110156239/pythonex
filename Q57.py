f = input("請選擇主餐與升級的套餐:")
w = input("是否升級成大杯飲料:")
s = input("是否換成大薯:")

A={"1A":127,"2A":117,"3A":137,"4A":99,"5A":115}
B={"1B":140,"2B":130,"3B":150,"4B":112,"5B":128}
if f in A and f == "1A":
    if w == "否" and s == "否":    
        print("總共為",A["1A"],"元")
    elif w == "是" and s == "是":
        print("總共為",A["1A"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",A["1A"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",A["1A"]+13,"元") 
if f in A and f == "2A":
    if w == "否" and s == "否":    
        print("總共為",A["2A"],"元")
    elif w == "是" and s == "是":
        print("總共為",A["2A"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",A["2A"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",A["2A"]+13,"元")
if f in A and f == "3A":
    if w == "否" and s == "否":    
        print("總共為",A["3A"],"元")
    elif w == "是" and s == "是":
        print("總共為",A["3A"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",A["3A"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",A["3A"]+13,"元") 
if f in A and f == "4A":
    if w == "否" and s == "否":    
        print("總共為",A["4A"],"元")
    elif w == "是" and s == "是":
        print("總共為",A["4A"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",A["4A"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",A["4A"]+13,"元")
if f in A and f == "5A":
    if w == "否" and s == "否":    
        print("總共為",A["5A"],"元")
    elif w == "是" and s == "是":
        print("總共為",A["5A"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",A["5A"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",A["5A"]+13,"元")   
      
if f in B and f == "1B":
    if w == "否" and s == "否":    
        print("總共為",B["1B"],"元")
    elif w == "是" and s == "是":
        print("總共為",B["1B"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",B["1B"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",B["1B"]+13,"元")
if f in B and f == "2B":
    if w == "否" and s == "否":    
        print("總共為",B["2B"],"元")
    elif w == "是" and s == "是":
        print("總共為",B["2B"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",B["2B"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",B["2B"]+13,"元")

if f in B and f == "3B":
    if w == "否" and s == "否":    
        print("總共為",B["3B"],"元")
    elif w == "是" and s == "是":
        print("總共為",B["3B"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",B["3B"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",B["3B"]+13,"元")
if f in B and f == "4B":
    if w == "否" and s == "否":    
        print("總共為",B["4B"],"元")
    elif w == "是" and s == "是":
        print("總共為",B["4B"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",B["4B"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",B["4B"]+13,"元")

if f in B and f == "5B":
    if w == "否" and s == "否":    
        print("總共為",B["5B"],"元")
    elif w == "是" and s == "是":
        print("總共為",B["5B"]+7+13,"元")
    elif w == "是" and s == "否":
        print("總共為",B["5B"]+7,"元") 
    elif w == "否" and s == "是":
        print("總共為",B["5B"]+13,"元")