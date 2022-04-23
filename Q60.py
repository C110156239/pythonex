txt = input("請輸入一串小寫英文:")

def en(txt):
    
  aeiou = txt.maketrans("aeiou", ".....", " ")

  txt = txt.translate(aeiou)
  print(txt)
  
en(txt)