u = []
for i in range(5):
  x = input("輸入牌值(最多五張):")
  if x == "A":
    x = 1 
  if x == "J":
    x = 11 
  if x == "Q":
    x = 12
  if x == "K":
    x = 13
  u.append(int(x))
print(sum(u))



