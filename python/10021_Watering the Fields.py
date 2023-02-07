'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	2054	547	415	27.593%
문제
Due to a lack of rain, Farmer John wants to build an irrigation system to send water between his N fields (1 <= N <= 2000).

Each field i is described by a distinct point (xi, yi) in the 2D plane,
 with 0 <= xi, yi <= 1000. 
 The cost of building a water pipe between two fields i and j is equal to the squared Euclidean distance between them:

(xi - xj)^2 + (yi - yj)^2

FJ would like to build a minimum-cost system of pipes so that all of his fields are linked together
 -- so that water in any field can follow a sequence of pipes to reach any other field.

Unfortunately, the contractor who is helping FJ install his irrigation system refuses to install any pipe unless its cost (squared Euclidean length) is at least C (1 <= C <= 1,000,000).

Please help FJ compute the minimum amount he will need pay to connect all his fields with a network of pipes.

입력
Line 1: The integers N and C.
Lines 2..1+N: Line i+1 contains the integers xi and yi.
출력
Line 1: The minimum cost of a network of pipes connecting the fields, or -1 if no such network can be built.
예제 입력 1 
3 11
0 2
5 0
4 3
예제 출력 1 
46

예제 입력 2
10 18
6 17
3 20
12 14
10 7
20 10
18 18
11 13
13 6
4 17
3 7
예제 출력 2
425
힌트
Input Details
There are 3 fields, at locations (0,2), (5,0), and (4,3). The contractor will only install pipes of cost at least 11.

Output Details
FJ cannot build a pipe between the fields at (4,3) and (5,0), since its cost would be only 10. 
He therefore builds a pipe between (0,2) and (5,0) at cost 29, and a pipe between (0,2) and (4,3) at cost 17.
'''
'''
메모리 초과
import sys
import heapq

N,C = map(int,sys.stdin.readline().split())
total = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    total.append([x,y])

q = []
for i in range(N):
    for j in range(i+1,N):
        # x^2 + y^2
        dis = int((total[i][0]-total[j][0])**2 + (total[i][1]-total[j][1])**2)
        if dis >= C:
            heapq.heappush(q,[dis,i,j])

visit = [False] * N
result = 0
while len(q):
    dist, i, j = heapq.heappop(q)
    if visit[i] == False or visit[j]==False:
        visit[i]=True
        visit[j]=True
        result +=dist
    else:
        continue
print(result)
'''
import sys
import math

N,C = map(int,sys.stdin.readline().split())
total = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    total.append([x,y])

# idx는 필요가 없었음
# idx = [i for i in range(N)]
D = [math.inf]*N
count = 1 
visit = [False] * N
next= 0
D[0]= 0
while count < N:
    # next 번째가 다음에 갈 것들 기록
    # j 번째는 next-j를 연결한 것과 이전것과 비교해서 작은 것
    # next번째는 방문하지 않은 것들중에서 가장 작은 것
    visit[next]=True
    min_val = math.inf
    for j in range(N):
        dis = (total[next][0]-total[j][0])**2 + (total[next][1]-total[j][1])**2
        if next!=j and dis >= C and D[j] > dis and visit[j] ==False:
            # 더 짧은 경로가 나온다면 업데이트
            D[j] = dis
            # idx[j]=next
            # j들중에서 가장 짧은 것이 next와 연결할 것
            if min_val > dis:
                min_val=dis
                # idx[next]=j
    # print(next)
    # print(D)
    # print(visit)
    # print(idx)
    
    # 방문하지 않은 것들중에서 다음으로 가장 작은것
    min_val = math.inf
    for i in range(N):
        if min_val > D[i] and visit[i]==False:
            min_val=D[i]
            next=i
    count+=1
# 찾지 못한다면 -1 , C보다 큰게 없다면 못 찾을 수 있음
if math.inf in D:
    print(-1)
else:
    print(sum(D))