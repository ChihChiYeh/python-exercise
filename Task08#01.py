x = int(input()) # 4
f = 0

def factorial(i):
    if i == 0:
       return 1
    else:
       return i * factorial(i-1)

for i in range(1, x+1):
    f += factorial(i)

print(f)
