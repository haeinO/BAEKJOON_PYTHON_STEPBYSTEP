case_num= int(input())
for i in range(case_num):
    grade=0
    count=1
    test_case=list(input())
    quiz = len(test_case)
    for i in range(quiz):
        if test_case[i]=='O':
           grade+=count
           count+=1
        else:
            count=1
    print(grade)
