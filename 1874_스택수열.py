import sys

n = int(sys.stdin.readline())
number = [i+1 for i in range(n)]
output = []
check = 0
stack=0
stack_list = []
for i in range(n):
    st = int(sys.stdin.readline().rstrip())
    
    # n개 까지 넣기
    while stack <= st:
        output.append('+')
        stack +=1
        stack_list.append(stack)

    if stack_list[-1] == st:
        output.append('-')
        stack_list.pop()

    # 맨 마지막 꺼가 pop되지 않고 쓰지 않을 것이 pop된다면
    # 결국 나중에 필요한 숫자를 pop을 못한다.
    else:
        check==1
        break
    '''
    나의 정답
    while True:
        if not st in number:
            check =1
            break
        if stack==0:
            stack +=1
            output.append('+')
        elif st == number[stack-1]:
            stack-=1
            output.append('-')
            del number[stack]
            break
        elif st > number[stack-1]:
            stack +=1
            output.append('+')
        elif st < number[stack-1]:
            stack -=1
            output.append('-')
            del number[stack]
    if check==1:
        break
    '''
if check==1:
    print('NO')
else:
    for i in output:
        print(i)