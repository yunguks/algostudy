"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	8365	3394	2450	40.813%
문제
봄버맨은 크기가 R×C인 직사각형 격자판 위에서 살고 있다. 격자의 각 칸은 비어있거나 폭탄이 들어있다.

폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며, 
인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도 함께 파괴된다. 
만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.

봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 모든 칸을 자유롭게 이동할 수 있다.
 봄버맨은 다음과 같이 행동한다.

가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
다음 1초 동안 봄버맨은 아무것도 하지 않는다.
다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
3과 4를 반복한다.
폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다.

예를 들어, 초기 상태가 아래와 같은 경우를 보자.

...
.O.
...
1초가 지난 후에는 아무 일도 벌어지지 않기 때문에, 위와 같다고 볼 수 있다. 1초가 더 흐른 후에 격자판의 상태는 아래와 같아진다.

OOO
OOO
OOO
1초가 지난 후엔 가운데에 있는 폭탄이 폭발해 가운데 칸과 인접한 네 칸이 빈 칸이 된다.

O.O
...
O.O
입력
첫째 줄에 R, C, N (1 ≤ R, C, N ≤ 200)이 주어진다. 둘째 줄부터 R개의 줄에 격자판의 초기 상태가 주어진다. 빈 칸은 '.'로, 폭탄은 'O'로 주어진다.

출력
총 R개의 줄에 N초가 지난 후의 격자판 상태를 출력한다.

예제 입력 1 
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....
예제 출력 1 
OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO
예제 입력 2 
6 7 4
.......
...O...
....O..
.......
OO.....
OO.....
예제 출력 2 
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
예제 입력 3 
6 7 5
.......
...O...
....O..
.......
OO.....
OO.....
예제 출력 3 
.......
...O...
....O..
.......
OO.....
OO.....

예제 출력 4
6 7 1
.......
...O...
....O..
.......
OO.....
OO.....

힌트
아래는 시간이 지난 후 예제 격자판의 상태이다.

.......
...O...
....O..
.......
OO.....
OO.....

<초기 상태, 1초 후>

OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO

<2초 후>

OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO

<3초 후>

OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO

<4초 후>

.......
...O...
....O..
.......
OO.....
OO.....

<5초 후>
"""
import sys

def info():
    r,c,n = list(map(int,sys.stdin.readline().split()))
    maps = []
    for _ in range(r):
        m = list(sys.stdin.readline().rstrip())
        if n !=1:
            for i in range(c):
                if m[i] ==".":
                    m[i] = 0
                else:
                    m[i] = 2
        maps.append(m)

    return r,c,n,maps

def sol(R,C,N,maps):
    if N==1:
        for i in range(R):
            print("".join(maps[i]))
        exit(0)
    plan = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(N-1):
        boom = []
        for y in range(R):
            for x in range(C):
                k = maps[y][x]
                if k==0:
                    if i%2==0:
                        maps[y][x]=3
                else:
                    maps[y][x] -=1
                    if k ==1:
                        boom.append([y,x])
        
        for y,x in boom:
            for p in plan:
                new_y = y +p[0]
                new_x = x +p[1]
                if R > new_y > -1 and C > new_x >-1:
                    maps[new_y][new_x]=0
        # print(i)
    for y in range(R):
        for x in range(C):
            if maps[y][x]==0:
                print(".",end="")
            else:
                print("O",end="")
        print()


if __name__=="__main__":
    R,C,N,maps = info()
    sol(R,C,N,maps)