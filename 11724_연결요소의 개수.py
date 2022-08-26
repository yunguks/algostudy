'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
'''

import sys
from collections import deque
def check(k):
    global s
    global visit
    q = deque()
    q.append(k)
    while q:
        temp = q.popleft()

        for i in s[temp]:
            if i not in visit:
                visit.append(i)
                q.append(i)
    
    return

input = sys.stdin.readline

N, M = map(int,input().split())
s = [[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    s[a].append(b)
    s[b].append(a)
visit =[]
count =0
for i in range(1,N+1):
    if i not in visit:
        count+=1
        visit.append(i)
        check(i)
print(count)