case=int(input())
for i in range(case):
    group=list(map(int,input().split()))
    a=len(group)-1
    score_sum=0
    count=0
    for i in range(a):
        score_sum+=group[i+1]
        average=score_sum/group[0]
    for i in range(a):
        if group[i+1]>average:
            count+=1
    print('%.3f' %(count/group[0]*100)+'%')
    
    
        
    
