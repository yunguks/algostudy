'''
문제
체스판 위에 한 나이트가 놓여져 있다. 
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
'''
import sys
from collections import deque

def bfs(n_i,n_j,t_i,t_j):
    global maps
    global l
    # 나이트는 1,2 칸 움직인다 ...
    plan =[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
    q = deque()
    q.append([n_i,n_j])
    while q:
        #print(q)
        x, y = q.popleft()

        for p in plan:
            new_x = x + p[0]
            new_y = y + p[1]
            if new_x <0 or new_y<0 or new_x > l-1 or new_y > l-1:
                continue
            if new_x==t_i and new_y==t_j:
                return maps[x][y]
            if maps[new_x][new_y]==0:
                q.append([new_x,new_y])
                maps[new_x][new_y] = maps[x][y]+1
    return 0

N = int(sys.stdin.readline())

for _ in range(N):
    l = int(sys.stdin.readline())
    # maps의 초기화
    maps = [[0 for _ in range(l)] for _ in range(l)]

    # 나이트의 시작지점
    n_i,n_j = map(int,sys.stdin.readline().split())
    maps[n_i][n_j]=1

    # 목표 지점
    t_i,t_j = map(int,sys.stdin.readline().split())

    if n_i==t_i and n_j==t_j:
        print(0)
    else:
        print(bfs(n_i,n_j,t_i,t_j))
