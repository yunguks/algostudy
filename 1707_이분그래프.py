'''
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

제한
2 ≤ K ≤ 5
1 ≤ V ≤ 20,000
1 ≤ E ≤ 200,000
예제 입력 1 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
예제 출력 1 
YES
NO
'''
import sys
from collections import deque

def check(s,visit,start):
    # BFS로 방문 queue 활용
    q = deque([start])
    visit[start]=1
    while q:
        temp = q.popleft()
        # 1, 2 그룹인지 찾기
        c = visit[temp]
        #print(start,temp,visit,s[temp])
        for i in s[temp]:
            #print(c,i,visit[i])
            # 방문안하였으면 추가하여 방문할 것
            if visit[i] ==0:
                visit[i] = 1 if c==2 else 2
                q.append(i)
            else:
            # 방문했었고 그 그룹이 같은 그룹에 속해있다면 false
                if c==visit[i]:
                    return 0

    return 1


input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    # 연결된 노드 초기화
    s =[[] for _ in range(V+1)]
    # 방문 초기화
    visit = [0 for _ in range(V+1)]
    # 연결할 노드 받기
    for _ in range(E):
        a,b = map(int,input().split())
        a, b= a, b
        s[a].append(b)
        s[b].append(a)
    #print(s)
    k =1
    for i in range(1,V+1):
        if visit[i]==0:
        # 다양한 곳에서 시작, 도중에 연결이 끊겨서 0으로 시작하는 부분이 있기 때문
        # 방문한 곳에 없다면 다시 시작
            if check(s,visit,i)==0:
                k=0
                break
    print('YES' if k else 'NO')