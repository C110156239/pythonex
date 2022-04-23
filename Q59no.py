a = int(input("輸入金額:"))

q = (a%100) 
w = ((a-100*q)%50) 
e = (a%10) // 5
r = (a%5) // 1
t = (a%1)


if q != 0:
    print("100元需要, " + str(q) + "個 ", end="")
if w != 0:
    print("50元需要, " + str(w) + "個 ", end="")
if e != 0:
    print("10元需要, " + str(e) + "個 ", end="")
if r != 0:
    print("5元需要, " + str(r) + "個 ", end="")
if t != 0:
    print("1元需要, " + str(t) + "個")

if a > 0:
    print("最少:",q+w+e+r+t)