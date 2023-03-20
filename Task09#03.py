def f(*args):
    result = 0
    for num in args:
        result += num
    return result

print(f(1, 2, 3)) # 6
print(f(1, 2, 3, 4, 5)) # 15
