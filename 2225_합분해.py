'''
문제
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

입력
첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

출력
첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
20 2
예제 출력 1 
21
예제 입력 2 
6 4
예제 출력 2 
84
'''

import sys

n, k = map(int,sys.stdin.readline().split())

# dp.shape (k,n) // k개에 n을 만들수 있는 경우는 각각 1개 씩 있다.
# 0*(n-1) + n*1 개
dp = [[1 for _ in range(n)] for _ in range(k)]

# n개를 k로 만드는 것은  k-1개에서 n-a를 만든 것에서 a를 더하는 것이다
# a = 0 도 가능하다
for i in range(1,k):
    for j in range(n):
        for y in range(j+1):
            dp[i][j]+=dp[i-1][y]%1000000000
        dp[i][j] = dp[i][j]%1000000000
print(dp[k-1][n-1])
'''
시간초과
def cal(n,k,count):
    global output
    a= sum(count)
    if a < k:
        b = count[:]
        b[0] = k-a
        # tuple로 저장 한 것은 중복 제거 하기 위함
        output.append(tuple(b))
    if a==k:
        output.append(tuple(count))

    for i in range(2,n+1):
        temp = count[:]
        if temp[1] >=i:
            temp[1] -=i
            temp[i] +=1
            cal(n,k,temp)

n, k = map(int,sys.stdin.readline().split())

count = [0 for i in range(n+1)]

fac = [0 for i in range(n+1)]
fac[0],fac[1] = 1,1
for i in range(2,n+1):
    fac[i]=fac[i-1]*i%1000000000

count[1]= n
output = []
cal(n,k,count)
sum=0
# tuple형으로 바꿔서 중복 제거
output = set(output)

for i in output:
    temp = fac[k]
    for j in i:
        temp = temp/fac[j]
    sum += temp %1000000000

print(int(sum))
'''