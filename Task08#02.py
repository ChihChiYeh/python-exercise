x = input() 
f = {}
for char in x:
    f[char] = f.get(char, 0)+1

print(f)
