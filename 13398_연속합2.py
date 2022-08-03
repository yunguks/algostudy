'''
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다. 또, 수열에서 수를 하나 제거할 수 있다. (제거하지 않아도 된다)

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 수를 제거하지 않았을 때의 정답은 12+21인 33이 정답이 된다.

만약, -35를 제거한다면, 수열은 10, -4, 3, 1, 5, 6, 12, 21, -1이 되고, 여기서 정답은 10-4+3+1+5+6+12+21인 54가 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
54
'''

import sys

input = sys.stdin.readline
n = int(input())
line = list(map(int,input().split()))

output =[[0,0,0]for _ in range(n)]
output[0]=[line[0],line[0],0]
for i in range(1,n):
    # 이전 입력
    out = output[i-1]
    # 현재 입력
    In = line[i]
    zero = out[0]+In
    one = out[1]+In
    two = out[2]

    if out[1]+In < In:
        one=In
        two = out[2]
    if In < 0:
        if out[2] >= In:
            zero = out[0]+out[2]
            two=In
    
    output[i]=[zero,one,two]
    print(output)

M = max(output[0][1],output[0][2])
for i in range(1,n):
    m = max(output[i])

    if M < m:
        M = m
print(M)