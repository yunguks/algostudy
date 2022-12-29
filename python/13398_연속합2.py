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
# 왼쪽에서 부터 i 까지의 최대값 + 오른쪽에서부터 i까지의 최대값 
# 두가지를 구하여서 i가 포함하는값 or 포함되지 않는 값 중에서 
# 최대값을 취한다
import sys

input = sys.stdin.readline
n = int(input())
line = list(map(int,input().split()))
# n-1 까지 합 중에서 최대, n+1 부터 합까지 최대 n을 제거 하였을 경우
if n==1:
    print(line[0])
    exit()

RR = [0]*(n)
LL = [0]*(n)
for i in range(n):
    if i==0:
        LL[0]=line[i]
    else:
        if LL[i-1]+line[i] < line[i]:
            LL[i]=line[i]
        else:
            LL[i]=LL[i-1]+line[i]

for j in range(n-1,-1,-1):
    if j==n-1:
        RR[j]=line[j]
    else:
        if RR[j+1]+line[j] < line[j]:
            RR[j]=line[j]
        else:
            RR[j]=RR[j+1]+line[j]
# print(LL)
# print(RR)
M = max(RR[1],RR[0])
for i in range(1,n-1):
    # a <= i 를 포함한 값
    a = LL[i]+RR[i]-line[i]
    # b <= i 를 포함하지 않은 값
    b = LL[i-1]+RR[i+1]
    if M < max(a,b):
        M = max(a,b)

if M < max(LL[n-1],LL[n-2]):
    M = max(LL[n-1],LL[n-2])
print(M)