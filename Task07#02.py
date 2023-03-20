x = input("請輸入一個數字：")

if not x.isdigit():
 print("輸入不合法！")
else:
    x = int(x)
 def factorial(n):
 if n == 0:
 return 1
 else:
 return n * factorial(n-1)
    f = factorial(x)
 print(f)
