'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
9
예제 출력 2 
55
'''
import sys

n = int(sys.stdin.readline())
# 1x2로 채운다면 2개의 직사각형을 사용하여 2칸
# 2x1로 채운다면 1개의 직사각형을 이용하여 1칸 채운다.
# n개면 2나 1을 더하여서 n을 만드는 데 몇개의 경우에 수가 있는지 확인
def cal(n):
    if n==1:
        return 1
    output = [0]*(n+1)
    output[0],output[1]=0,1
    output[2]=2
    for i in range(3,n+1):
        output[i]=output[i-1]+output[i-2]
    # if n>1: 시간초과, 하나씩 다 보는 top-down
    #     return cal(n-2)+cal(n-1)
    # else:
    #     return 1
    return output[n]

print(cal(n)%10007)