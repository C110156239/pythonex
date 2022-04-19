import re
text = input('請輸入自傳:')    # 新增 text 變數，記錄輸入的字串
w = re.sub(r'[^\w\s]','',text) 
repeat = []                          # 新增 repeat 變數為空串列
                     
for i in w:                        # 使用 for 迴圈，依序取出每個字元                   
  a = w.count(i, 0, len(w))     # 判斷字元在字串中出現的次數
  if a>1 and i not in repeat:         # 如果次數大於 1，且沒有存在 repeat 串列中
    repeat.append(i)                  # 將字元加入 repeat 串列春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。

print(repeat)
