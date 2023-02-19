"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	65257	18016	12840	27.795%
문제
여행을 떠난 세준이는 지도를 하나 구하였다. 
이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며,
  각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.

현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다.
 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 
 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 
제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 
이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. 
M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

출력
첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.

예제 입력 1 
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
예제 출력 1 
3

예제 입력2
4 4
16 9 8 1
15 10 7 2
14 11 6 3
13 12 5 4
예제 출력 2
10
"""

import sys
def info():
    M,N= map(int,sys.stdin.readline().split())
    maps=[]
    for _ in range(M):
        maps.append(list(map(int,sys.stdin.readline().split())))
    return M,N,maps

def sol(M,N,maps):
    result = [[0 for _ in range(N)] for _ in range(M)]
    result[0][0] = 1

    for y in range(M):
        for x in range(N):
            # 위에서 아래로 내려올 때
            if y > 0 :
                if maps[y-1][x] > maps[y][x]:
                    result[y][x]+=result[y-1][x]
                
            # 왼쪽에서 오른쪽으로 갈때
            if x > 0 and maps[y][x-1] > maps[y][x]:
                result[y][x]+=result[y][x-1]

            add = result[y][x]
            stack = []
            visit = [y,x]
            # 아래에서 위로 갈 때
            if [1,1]==visit:
                print(result[1][1])
                exit(0)
            if y > 0 and maps[y-1][x] < maps[y][x]:
                stack.append([y-1,x])
            
            # 오른쪽에서 왼쪽
            if x > 0 and maps[y][x-1] < maps[y][x]:
                stack.append([y,x-1])
            plan = [[0,-1],[-1,0],[0,1],[1,0]]
            while len(stack)> 0:
                new_y,new_x = stack.pop()
                if [new_y,new_x] not in visit:
                    visit.append([new_y,new_x])
                    result[new_y][new_x]+=add
                    for p in plan:
                        make_y = p[0]+new_y
                        make_x = p[1]+new_x
                        if -1 < make_y <y:
                            if maps[make_y][make_y] < maps[new_y][new_x]:
                                stack.append([make_y,make_x])
                        elif make_y == y and -1 <make_x < x:
                            if maps[make_y][make_y] < maps[new_y][new_x]:
                                stack.append([make_y,make_x])

                else:
                    continue
            for i in result:
                print(i)
            print()

    return  result[-1][-1]

if __name__=="__main__":
    print(sol(*info()))