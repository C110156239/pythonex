# n = int(input())
# arr = []
# for i in range(n):
# 	arr.append(list(map(int, input().rstrip().split())))
# w = sorted(arr)
# print(w)  score=[[0]*40 for i in range(5)]



a = int(input("輸入甲方的值:"))
b = int(input("輸入乙方的值:"))
arr = []
for i in range(a,b):
	arr.append(list(map(int, input().rstrip().split(" "))))
  
print(arr)