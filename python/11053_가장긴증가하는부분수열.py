'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
예제 입력 2
7
10 20 9 30 10 12 13
'''
# i번째 보다 앞에 나온 숫자중에서 작은 수만 본다. 차례대로 커져야 하기 때문
# 또한 그중에서도 수열의 길이가 가장 큰 것을 찾아 +1 한다
import sys

n=int(sys.stdin.readline())

line = list(map(int,sys.stdin.readline().split()))
output = [1]

for i in range(1,n):
    max = 0
    for j in range(i):
        if line[i]> line[j]:
            if max < output[j]:
                max = output[j]
    output.append(max+1)
    
max = 0
for i in output:
    if max < i:
        max = i
print(max)

'''
# 큰수가 나오면 업데이트 하여 찾기, 이렇게 되면 큰 수를 건너띄고 만들 었을떄 더 긴 배열이 되므로
# 그것은 고려하지 않음
line = list(map(int,sys.stdin.readline().split()))
output=[[1,i] for i in line]
for i in range(1,n): 
    print(i,end ='  ')
    for j in range(i):
        print(j,end=' ')
        if output[i][1] > output[j][1]:
            output[j][0] +=1
            output[j][1] = output[i][1]
    print(output[i][1],output) 
max = 0
for i in output:
    if max < i[0]:
        max = i[0]
print(max)
'''