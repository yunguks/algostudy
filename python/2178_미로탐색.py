'''
문제
NxM크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 
최소의 칸 수를 구하는 프로그램을 작성하시오.
 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13`
'''
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
maps=[]
for i in range(N):
    maps.append(list(map(int,sys.stdin.readline().rstrip())))
mincount = N*M
def move(i,j,maps):
    global N, M
    q = deque([[i,j]])
    plan = [[0,1],[1,0],[-1,0],[0,-1]]
    
    while q:
        temp = q.popleft()
        x = temp[0]
        y = temp[1]
        for p in plan:
            new_i = x + p[0]
            new_j = y + p[1]
            if new_i <0 or new_j<0 or new_i>N-1 or new_j>M-1:
                continue
            if maps[new_i][new_j]==1:
                q.append([new_i,new_j])
                maps[new_i][new_j] = maps[x][y]+1
            # elif maps[new_i][new_j]>1:
            #     q.append([new_i,new_j])
            #     maps[new_i][new_j] = min(maps[x][y]+1,maps[new_i][new_j])

    return maps[N-1][M-1]        

print(move(0,0,maps))
# for i in maps:
#     print(*i)
# dfs 는 시간초과
# def move(i,j,maps,count):
#     global N,M
#     global mincount
#     #print(i,j)
#     if i==N-1 and j==M-1:
#         return count

#     v= [item[:] for item in maps]
    
#     plan = [[0,1],[1,0],[-1,0],[0,-1]]
#     for p in plan:
#         new_i = i + p[0]
#         new_j = j + p[1]
#         if new_i <0 or new_j <0 or new_i>N-1 or new_j>M-1:
#             continue
#         if v[new_i][new_j]==1:
#             # 방문한 노드 되돌아 오지 않도록 0 설정
#             v[new_i][new_j]=0
#             mincount = min(mincount,move(new_i,new_j,v,count+1))
    
#     return mincount