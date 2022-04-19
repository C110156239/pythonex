import re
wang = "「紅豆生南國，春來發幾枝?願君多采擷，此物最相思。」" 
mon = "「春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。」" 
w = re.sub(r'[^\w\s]','',wang)
h = re.sub(r'[^\w\s]','',mon)
res = []
for x in w:
    if x in h:
        res.append(x)
print (res) 