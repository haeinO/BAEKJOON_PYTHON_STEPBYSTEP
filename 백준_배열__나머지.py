num=[]
for i in range(10):
    num.append(input())
re=[int(num[i])%42 for i in range(10)]
over=len(set(re))
print(over)
