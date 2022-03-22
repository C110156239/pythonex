# tmp = [1,3,5,7]
# tmp1 = (1,3,5,7)
# print(tmp)

import random

grade = []
for i in range(1,56):
    grade.append(random.randint(0, 100))

tmpk="C1101562"
id = []
for i in range(1,56):
    id.append(tmpk+'{0:02d}'.format(i))

tmp2 = {"C110156239":{"國文":100,"英文":95,"程式":80},"C110156222":{"國文":0,"英文":10,"程式":3},"C110156215":0,"C110156214":1,"C110156299":"帥哥"}


print(grade[0])
print(tmp2['C110156239'])

tmp2['C110156239']['國文'] = 80 
tmp2['C110156215'] = 1
tmp2['C110156299'] = "醜男"

tmp3 = {}
for i in range(1,56):
    tmp3[id[i]]=grade[i]