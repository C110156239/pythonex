a = int(input('輸入整數n:'))

e = a // 2

for i in range(-e,e+1):

  j = abs(i)

  print(' '*j + '*'*(a-j*2) + ' '*j)

