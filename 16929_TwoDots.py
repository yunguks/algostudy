'''
각각의 칸은 색이 칠해진 공이 하나씩 있다. 이 게임의 핵심은 같은 색으로 이루어진 사이클을 찾는 것이다.

다음은 위의 게임판에서 만들 수 있는 사이클의 예시이다.

점 k개 d1, d2, ..., dk로 이루어진 사이클의 정의는 아래와 같다.

모든 k개의 점은 서로 다르다. 
k는 4보다 크거나 같다.
모든 점의 색은 같다.
모든 1 ≤ i ≤ k-1에 대해서, di와 di+1은 인접하다. 또, dk와 d1도 인접해야 한다. 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미이다.
게임판의 상태가 주어졌을 때, 사이클이 존재하는지 아닌지 구해보자.

입력
첫째 줄에 게임판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다. 게임판은 모두 점으로 가득차 있고, 게임판의 상태는 점의 색을 의미한다. 점의 색은 알파벳 대문자 한 글자이다.

출력
사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"를 출력한다.

제한
2 ≤ N, M ≤ 50
예제 입력 1 
3 4
AAAA
ABCA
AAAA
예제 출력 1 
Yes
예제 입력 2 
3 4
AAAA
ABCA
AADA
예제 출력 2 
No
예제 입력 3 
4 4
YYYR
BYBY
BBBY
BBBY
예제 출력 3 
Yes
예제 입력 4 
7 6
AAAAAB
ABBBAB
ABAAAB
ABABBB
ABAAAB
ABBBAB
AAAAAB
예제 출력 4 
Yes
예제 입력 5 
2 13
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
예제 출력 5 
No
'''
import sys
#import numpy as np

N, M = map(int,sys.stdin.readline().split())

maps = []
for i in range(N):
    maps.append(list(sys.stdin.readline().rstrip()))

plan =[[0,1],[1,0],[0,-1],[-1,0]]

def dfs(start,now,cha,count,check):
    global maps
    global plan
    global N,M
    #print(np.array(check))
    if start[0]==now[0] and start[1]==now[1] and count >3:
        return 1
    

    for p in plan:
        nx = now[0]+p[0]
        ny = now[1]+p[1]
        # nx,ny 범위를 넘어서지 않고
        # 방문하지 않고, 다음 갈 곳의 문자가 처음과 같다면
        if (-1 < nx < N) and (-1 < ny < M) and check[nx][ny]==0 and maps[nx][ny]==cha:
            check[nx][ny]=1
            if dfs(start,[nx,ny],cha,count+1,check):
                return 1
    return 0

for i in range(N):
    for j in range(M):
        if maps[i][j]!='0':
            # 매번 방문 한 곳 초기화
            check = [[0 for _ in range(M)] for _ in range(N)]
            if dfs([i,j],[i,j],maps[i][j],1,check):
                print('Yes')
                exit()
            
print('No')