'''
문제
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 30 10 20 20 10
예제 출력 1 
3
'''
import sys
input= sys.stdin.readline
n = int(input())
line = list(map(int,input().split()))
output = [[line[0],1]]
for i in range(1,n):
    M = 0
    # i보다 먼저 나온 수들을 보면서 i 보다 크고, 길이가 가장 큰 값에서 +1
    for j in range(i):
        if line[i] < output[j][0]:
            if M < output[j][1]:
                M = output[j][1]    
    output.append([line[i],M+1])
#print(output)
print(max(x[1] for x in output))