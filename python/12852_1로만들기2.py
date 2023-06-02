"""
1로 만들기 2 스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	22600	10529	8431	47.182%
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1 
2
예제 출력 1 
1
2 1
예제 입력 2 
10
예제 출력 2 
3
10 9 3 1
"""
import sys
from collections import deque

if __name__=="__main__":
    N = int(sys.stdin.readline().rstrip())
    
    count=[0]*(N+1)
    visit=[i-1 for i in range(N+1)]
    count[1]=1
    visit[1]=0
    for i in range(2,N+1):
        
        count[i]=count[i-1]+1
        
        if i%3==0:
            if count[i//3]+1 < count[i]:
                count[i]=count[i//3]+1
                visit[i]=i//3
        if i%2==0:
            if count[i//2]+1 < count[i]:
                count[i]=count[i//2]+1
                visit[i]=i//2
    
    print(count[-1]-1)
    j=N
    while True:
        v = visit[j]
        print(j, end=" ")
        if v ==0:
            break
        j = v
                
    
    # q = deque()
    # q.append([N])
    # result = N
    # output = []
    # while len(q)>0:
    #     num = q.popleft()
    #     f = num[0]
    #     if f==1:
    #         if result >= len(num):
    #             result = len(num)
    #             output = num[:]
    #             break
    #     # 3으로 나눠질 때
    #     if f%3 ==0:
    #         q.append([f//3]+num)
    #     if f%2 ==0:
    #         q.append([f//2]+num)
    #     if f > 1:
    #         q.append([f-1]+num)
    
    # print(result-1)
    # print(*output[::-1])