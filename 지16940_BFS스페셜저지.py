'''
문제
BOJ에서 정답이 여러가지인 경우에는 스페셜 저지를 사용한다. 스페셜 저지는 유저가 출력한 답을 검증하는 코드를 통해서 정답 유무를 결정하는 방식이다. 오늘은 스페셜 저지 코드를 하나 만들어보려고 한다.

정점의 개수가 N이고, 정점에 1부터 N까지 번호가 매겨져있는 양방향 그래프가 있을 때, BFS 알고리즘은 다음과 같은 형태로 이루어져 있다.

큐에 시작 정점을 넣는다. 이 문제에서 시작 정점은 1이다. 1을 방문했다고 처리한다.
큐가 비어 있지 않은 동안 다음을 반복한다.
큐에 들어있는 첫 정점을 큐에서 꺼낸다. 이 정점을 x라고 하자.
x와 연결되어 있으면, 아직 방문하지 않은 정점 y를 모두 큐에 넣는다. 모든 y를 방문했다고 처리한다.
2-2 단계에서 방문하지 않은 정점을 방문하는 순서는 중요하지 않다. 따라서, BFS의 결과는 여러가지가 나올 수 있다.

트리가 주어졌을 때, 올바른 BFS 방문 순서인지 구해보자.

입력
첫째 줄에 정점의 수 N(2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에는 트리의 간선 정보가 주어진다. 마지막 줄에는 BFS 방문 순서가 주어진다. BFS 방문 순서는 항상 N개의 정수로 이루어져 있으며, 1부터 N까지 자연수가 한 번씩 등장한다.

출력
입력으로 주어진 BFS 방문 순서가 올바른 순서면 1, 아니면 0을 출력한다.

예제 입력 1 
4
1 2
1 3
2 4
1 2 3 4
예제 출력 1 
1
올바른 순서는 1, 2, 3, 4와  1, 3, 2, 4가 있다.

예제 입력 2 
4
1 2
1 3
2 4
1 2 4 3
예제 출력 2 
0
'''

import sys
from collections import deque
def BFS(S,answer):
    global N
    q = deque([0])
    visit = [0]*N
    if answer[0]!=0:
        return 0
    i = 1
    visit[0]=1
    while q:
        k = q.popleft()
        while i<N:
            # i번째 답이 S[k]에 있다면 q에 넣어서
            if answer[i] in S[k] and visit[answer[i]]==0:
                q.append(answer[i])
                visit[answer[i]]=1
                i+=1
            # 없다면 다음으로 넘어가기
            else:
                break
    # 모두 방문했다면 올바름
    for i in range(N):
        if visit[i]==0:
            return 0
    return 1

N = int(sys.stdin.readline())

S = [[] for _ in range(N)]
for _ in range(N-1):
    a,b= list(map(int,sys.stdin.readline().split()))
    S[a-1].append(b-1)
    S[b-1].append(a-1)

answer = list(map(int,sys.stdin.readline().split()))
for i in range(N):
    answer[i] -=1
print(BFS(S,answer))

