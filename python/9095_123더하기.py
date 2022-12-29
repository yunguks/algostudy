'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
'''
# [1,2,3] 각각의 1의 개수 2의 개수 3의 개수가 몇개 있는 지 나타내는 배열을 만든다.
# 총 개수를 순서 + 중복된 수를 제거하는 순열로 계산을 하였다
# 배열을 만드는데는 처음 [n,0,0] 에서
# [n-2,1,0], [n-3,0,1] 방식으로 계산하였음.

# **간단한 풀이가 아래에 있음.
# i는 i-1, i-2, i-3 을 더한 것 
#     1이 추가, 2가 추가, 3이 추가 된 것에서 순서를 매긴다.
# output[i-1]개 에서 1이 추가되는 경우의 수는 output[i-1]개와 동일하다
import sys

def cal(n,b,c):
    global output
    if not [n,b,c] in output:
        output.append([n,b,c])
    if n>2:
        cal(n-3,b,c+1)
    if n>1:
        cal(n-2,b+1,c)

def factorial(n):
    if n <2:
        return [1,1]
    fac = [1]*(n+1)
    fac[2]=2
    for i in range(3,n+1):
        fac[i]= fac[i-1]*i
    return fac

k = int(sys.stdin.readline())
for _ in range(k):
    n = int(sys.stdin.readline())
    output =[]
    fac = factorial(n)
    cal(n,0,0)
    count = 0
    for i in output:
        a,b,c = i
        count += fac[a+b+c]/fac[a]/fac[b]/fac[c]
    print(int(count))
'''
k = int(sys.stdin.readline())
output =[0]*11
output[1]=1
output[2]=2
output[3]=4
for _ in range(k):
    n = int(sys.stdin.readline())
    for i in range(4,n+1):
        output[i]=output[i-1]+output[i-2]+output[i-3]
    print(output[n])
'''
