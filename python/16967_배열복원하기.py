"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	2708	1253	1013	45.324%
문제
크기가 H x W인 배열 A와 두 정수 X와 Y가 있을 때, 
크기가 (H + X) x (W + Y)인 배열 B는 배열 A와 배열 A를 아래로 X칸, 
오른쪽으로 Y칸 이동시킨 배열을 겹쳐 만들 수 있다. 수가 겹쳐지면 수가 합쳐진다.

즉, 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나이다.

(i, j)가 두 배열 모두에 포함되지 않으면, Bi,j = 0이다.
(i, j)가 두 배열 모두에 포함되면, Bi,j = Ai,j + Ai-X,j-Y이다.
(i, j)가 두 배열 중 하나에 포함되면, Bi,j = Ai,j 또는 Ai-X,j-Y이다.
배열 B와 정수 X, Y가 주어졌을 때, 배열 A를 구해보자.

입력
첫째 줄에 네 정수 H, W, X, Y가 주어진다. 둘째 줄부터 H + X개의 줄에 배열 B의 원소가 주어진다.

항상 배열 A가 존재하는 경우만 입력으로 주어진다.

출력
총 H개의 줄에 배열 A의 원소를 출력한다.

제한
2 ≤ H, W ≤ 300
1 ≤ X < H
1 ≤ Y < W
0 ≤ Bi,j ≤ 1,000

예제 입력 1 
2 4 1 1
1 2 3 4 0
5 7 9 11 4
0 5 6 7 8
예제 출력 1 
1 2 3 4
5 6 7 8
예제 입력 2 
3 3 2 1
1 2 3 0
4 5 6 0
7 9 11 3
0 4 5 6
0 7 8 9
예제 출력 2 
1 2 3
4 5 6
7 8 9

예제 입력 3
3 3 2 2
1 2 3 0 0
4 5 6 0 0
7 8 10 2 3
0 0 4 5 6
0 0 7 8 9
예제 출력 3
1 2 3
4 5 6
7 8 9
"""

import sys

H,W,X,Y = map(int,sys.stdin.readline().split())

matrix = []
for _ in range(H+X):
    matrix.append(list(map(int,sys.stdin.readline().split())))

result = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    for w in range(W):
        if w >= Y and h >=X:
            result[h][w] = matrix[h][w]-result[h-X][w-Y]
        else:
            result[h][w] = matrix[h][w]
for i in range(len(result)):
    print(*result[i])