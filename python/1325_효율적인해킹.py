"""
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

예제 입력 1 
5 4
3 1
3 2
4 3
5 3
예제 출력 1 
1 2
"""
import sys
from collections import deque

if __name__=="__main__":
    N, M = map(int,sys.stdin.readline().split())

    tree = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int,sys.stdin.readline().split())
        tree[b].append(a)
    
    def bfs(start):
        q = deque([start])
        visit = [False]*(N+1)
        visit[start] = True
        count = 1

        while q:
            next = q.popleft()
            for node in tree[next]:
                if not visit[node]:
                    visit[node]=True
                    q.append(node)
                    count+=1
        return count       

    result = [] 
    Max = 0
    for i in range(1,N+1):
        c = bfs(i)
        if Max < c:
            result= [i]
            Max = c
        elif Max == c:
            result.append(i)
        # result.append([i,bfs(i)])

    # result = sorted(result, key=lambda x:x[1], reverse=True)
    print(*result)

    # for i in range(N):
    #     if Max == result[i]:
    #         print(i+1, end=" ")