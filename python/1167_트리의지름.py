# -*- coding: utf-8 -*-
'''
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1 
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력 1 
11
'''
import sys
import heapq

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
# print(tree)
# print(visit)

q = []

for _ in range(N):
    v = list(map(int,sys.stdin.readline().split()))
    c = 1
    while v[c]!=-1:
        # tree [v, length]
        tree[v[0]].append([v[c],v[c+1]])
        heapq.heappush(q,[-v[c+1], v[c], v[0]])
        c+=2

def finding(length, vertex,visit):
    global max_length

    for v,l in tree[vertex]:
        if visit[v]==0:
            new_visit = visit[:]
            new_length = length+l
            # print(f"v : {v}, new_length : {new_length}")
            new_visit[v]=1
            finding(new_length,v,new_visit)

    max_length = max(length, max_length)

a, b, c = heapq.heappop(q)
visit[b]=1
max_length = 0
# print(f"first {b}")
finding(0,b,visit)
# print(max_length)
visit = [0 for _ in range(N+1)]
visit[c]=1
# print(f"first {c}")
finding(0,c,visit)
print(max_length)