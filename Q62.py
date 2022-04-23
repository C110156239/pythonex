dict1 = {"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}

i = input("請輸入水果:")

if i == "蘋果":
    print("蘋果是",dict1["蘋果"])

elif i == "香蕉":
    print("香蕉是",dict1["香蕉"])

elif i == "葡萄":
    print("葡萄是",dict1["葡萄"])

elif i == "藍莓":
    print("藍莓是",dict1["藍莓"])

elif i == "橘子":
    print("橘子是",dict1["橘子"])

else:
    print("不再字典裡")