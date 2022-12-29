'''
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다.

예제 입력 1 
2
예제 출력 1 
3
'''
import sys
# 세가지 경우
# 1. 2칸 만들 수 있는 것들로 다 하는 경우
# 2. 4,6,8 칸 만들 수 있는 것들로 2개씩 만들 수 있음
# 3. n칸의 특수한 경우 2개를 만들수 있음
input = sys.stdin.readline
n = int(input())

output =[0]*(n+1)
if n==1:
    print(0)
    exit()
output[2]=3
for i in range(4,n+1,2):
    output[i] = 3*output[i-2]
    
    for j in range(0,i-4+1,2):
        output[i]+=output[j]*2
    
        # print(i,j)
    output[i] +=2
print(output[n])

