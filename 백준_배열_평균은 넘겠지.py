case=int(input())
for i in range(case):
    group=list(map(int,input().split()))
    a=group[1:]
    b=len(a)
    score_sum=0
    count=0
    for i in range(b):
        score_sum+=group[i+1]
    average=score_sum/group[0]
    for i in range(b):
        if group[i+1]>average:
            count+=1
    rate=round(count/group[0]*100,3)
    print('%.3f' %rate+'%')
    
    
        
    
