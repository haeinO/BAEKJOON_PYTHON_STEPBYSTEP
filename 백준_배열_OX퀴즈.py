case_num= int(input())
for i in range(case_num):
    grade=0
    count=1
    test_case=input() #input의 default type은 str, str은 인덱싱이 가능하기 때문에 굳이 list로 형변환을 하지 않아도 됨
    quiz = len(test_case)
    for i in range(quiz):
        if test_case[i]=='O':
           grade+=count
           count+=1
        else:
            count=1
    print(grade)
