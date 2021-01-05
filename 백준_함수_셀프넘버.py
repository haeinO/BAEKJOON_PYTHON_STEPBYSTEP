def dn(n):
    num=n
    while n!=0:
        num+=n%10
        n=int(n/10)
    return num

self_num=[i for i in range(1,10001)]
for i in range(10001):
    if dn(i) in self_num:
        self_num.remove(dn(i))
for i in range(len(self_num)):
    print(self_num[i])
    
        
