'''
문제
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

예제 입력 1 
10
1 100 2 50 60 3 5 6 7 8
예제 출력 1 
113
'''

import sys

input = sys.stdin.readline

n=int(input())

line = list(map(int,input().split()))
output = [[line[0]]]
for i in range(1,len(line)):
    if min(line[:i]) > line[i]:
        output.append([line[i]])
    for j in range(len(output)):
        if output[j][-1] < line[i]:
            output.append(output[j]+[line[i]])

M = 0
for i in output:
    if M < sum(i):
        M = sum(i)
print(M)