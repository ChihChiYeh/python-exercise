L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_num=[]
even_num=[]

for x in range(len(L)):
 if x % 2 ==0:
        even_num.append(x)
 else:
        odd_num.append(x)
L = odd_num+even_num

print(L)
