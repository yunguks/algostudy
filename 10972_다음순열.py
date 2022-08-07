'''
문제
1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
1 2 4 3
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
-1
'''

import sys

input = sys.stdin.readline
N = int(input())
ans = list(map(int,input().split()))
order = [i+1 for i in range(N)]

def check(input,ans,c,N):
    global order
    if c ==-1:
        return -1

    if input == ans:
        print(input,ans)
        c =1
        return c
    if len(input) <N:

        for i in range(N):
            if order[i] not in input:
                input.append(order[i])
                if c==1 and len(input)==N:
                    print(*input)
                    return -1
                c = check(input,ans,c,N)
                input.pop()
    return c
if ans == sorted(order,reverse=True):
    print(-1)
else:
    check([],ans,0,N)

