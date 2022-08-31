'''
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9
'''
# 방문 노드를 계산하지 않고 maps을 1에서 0으로 바꿔줌으로써
# 다시 방문하지 못하도록 함
import sys
from collections import deque

def check(i,j):
    global maps
    q = deque([[i,j]])
    # 위 아래 양옆 대각선 방문 계획
    plan = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
    while q:
        # 방문  
        i, j = q.popleft()

        for p in plan:
            new_i = i +p[0]
            new_j = j +p[1]
            if new_i <0 or new_i >len(maps)-1 or new_j<0 or new_j >len(maps[0])-1:
                continue
            if maps[new_i][new_j]==1:
                # 방문한 곳은 maps를 0으로 바꿔 다시 방문하지 않도록
                maps[new_i][new_j]=0
                q.append([new_i,new_j])

input = sys.stdin.readline
while True:
    a, b = map(int,input().split())
    if a == 0 or b==0:
        break
    
    # 지도 초기화
    # a 열(너비), b가 행(높이)
    maps = []
    # 지도 받기
    for i in range(b):
        if a==1:
            maps.append(list(map(int,input().rstrip())))
        else:
            maps.append(list(map(int,input().split())))

    # 섬 개수 세기
    count = 0
    for i in range(b):
        for j in range(a):
            if maps[i][j]==1:
                check(i,j)
                count +=1
    print(count)