
# answer = list(input('輸入四個數字答案：'))
# print(answer)
# a = b = n = 0     
# while a!=4:       
#   a = b = n = 0   
#   user = list(input('輸入四個數字：'))  
#   for i in user:                   
#     if int(user[n]) == answer[n]:    
#       a += 1                        
#     else:
#       if int(i) in answer:           
#         b += 1                       
#     n += 1                           
#   output = ','.join(user).replace(',','')    
#   print(f'{output}: {a}A{b}B')


que= list(input('輸入四個數字答案：'))
ans= list(input('輸入四個數字：')) 
a=0
b=0
for i in range(4):
    if que[i] in ans:
          b=b+1     
    if que[i] == ans[i]:
          a = a+1     
print(a,"A",b,"B")
