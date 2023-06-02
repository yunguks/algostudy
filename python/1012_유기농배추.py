"""
유기농 배추

1 초	512 MB	148871	59276	39785	37.693%
문제

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1 
5
1
예제 입력 2 
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
예제 출력 2 
2

"""
from collections import deque
import sys

if __name__=="__main__":
    T = int(sys.stdin.readline().rstrip())
    plan = [[0,1],[1,0],[-1,0],[0,-1]]
    for i in range(T):
        count = 0
        M, N, K = map(int,sys.stdin.readline().split())
        target = []
        visit = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int,sys.stdin.readline().split())
            visit[y][x] = 1
            target.append([x,y])
            
        for x,y in target:
            q = deque([])
            if visit[y][x]:
                q.append([x,y])
                while q:
                    new_x,new_y = q.popleft()
                    
                    if visit[new_y][new_x]:
                        visit[new_y][new_x]=0
                    else:
                        continue
                    for px,py in plan:
                        if -1 <(new_x+px)<M and -1<(new_y+py)<N:
                            if visit[new_y+py][new_x+px]:
                                q.appendleft([new_x+px,new_y+py])
                count+=1
                
        print(count)