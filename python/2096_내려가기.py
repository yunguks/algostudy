"""
내려가기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	4 MB (하단 참고)	32350	12294	9567	36.613%
문제
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 
이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 
그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다.
 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 
 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.

별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 
빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 
최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다.
 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

출력
첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

예제 입력 1 
3
1 2 3
4 5 6
4 9 0
예제 출력 1 
18 6
예제 입력 2 
3
0 0 0
0 0 0
0 0 0
예제 출력 2 
0 0
"""

import sys

def sol():
    N = int(sys.stdin.readline().rstrip())
    max_before = [0]*3
    max_now = [0]*3
    min_before = [0]*3
    min_now = [0]*3
    for _ in range(N):
        l = list(map(int,sys.stdin.readline().split())) # [1,2,3]
            # print(l)
        max_now[0]=max(max_before[0:2]) + l[0]
        max_now[1]=max(max_before) +l[1]
        max_now[2]=max(max_before[1:]) +l[2]
        max_before = max_now[:]
        
        min_now[0]=min(min_before[0:2]) + l[0]
        min_now[1]=min(min_before) +l[1]
        min_now[2]=min(min_before[1:]) +l[2]
        min_before = min_now[:]

    max_v = max(max_now)
    min_v = min(min_now)
    return max_v, min_v

if __name__=="__main__":
    print(*sol())