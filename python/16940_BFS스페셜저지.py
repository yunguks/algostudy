'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	7688	2064	1242	24.473%
문제
BOJ에서 정답이 여러가지인 경우에는 스페셜 저지를 사용한다. 
스페셜 저지는 유저가 출력한 답을 검증하는 코드를 통해서 정답 유무를 결정하는 방식이다.
 오늘은 스페셜 저지 코드를 하나 만들어보려고 한다.

정점의 개수가 N이고, 정점에 1부터 N까지 번호가 매겨져있는 양방향 그래프가 있을 때,
 BFS 알고리즘은 다음과 같은 형태로 이루어져 있다.

큐에 시작 정점을 넣는다. 이 문제에서 시작 정점은 1이다. 1을 방문했다고 처리한다.
큐가 비어 있지 않은 동안 다음을 반복한다.
큐에 들어있는 첫 정점을 큐에서 꺼낸다. 이 정점을 x라고 하자.
x와 연결되어 있으면, 아직 방문하지 않은 정점 y를 모두 큐에 넣는다. 
모든 y를 방문했다고 처리한다.
2-2 단계에서 방문하지 않은 정점을 방문하는 순서는 중요하지 않다. 
따라서, BFS의 결과는 여러가지가 나올 수 있다.

트리가 주어졌을 때, 올바른 BFS 방문 순서인지 구해보자.

입력
첫째 줄에 정점의 수 N(2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에는 트리의 간선 정보가 주어진다. 
마지막 줄에는 BFS 방문 순서가 주어진다. BFS 방문 순서는 항상 N개의 정수로 이루어져 있으며,
 1부터 N까지 자연수가 한 번씩 등장한다.

출력
입력으로 주어진 BFS 방문 순서가 올바른 순서면 1, 아니면 0을 출력한다.

예제 입력 1 
4
1 2
1 3
2 4
1 2 3 4
예제 출력 1 
1
올바른 순서는 1, 2, 3, 4와  1, 3, 2, 4가 있다.

예제 입력 2 
4
1 2
1 3
2 4
1 2 4 3
예제 출력 2 
0

예제 입력 3
7
1 2
1 3
2 4
2 5
3 6
3 7
1 3 2 4 5 6 7

예제 출력
0

7
1 2
1 3
2 4
2 5
3 6
3 7
1 3 2 6 7 5 4

1
'''
from collections import deque
import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
check = list(map(int,sys.stdin.readline().split()))
# check.reverse()
if check[0]!=1:
    print(0)
    exit(0)
else:
    if len(check)==1:
        print(1)
        exit(0)
visit = [False] *(N+1)
visit[0]=True
order = deque([1])
count = 1
child = [[] for _ in range(N+1)]
while len(order)> 0:
    new = order.popleft()
    visit[new]=True
    
    for i in tree[new]:
        if visit[i] == False:
            child[new].append(i)
            order.append(i)
# print(child)
q = deque([1])
result = []
count = 1

while len(q) > 0:
    next = q.popleft()
    length = len(child[next])
    # print(next, count, length)
    # print(set(child[next]))
    # print(set(check[count:count+length]))
    if set(child[next]) != set(check[count:count+length]):
        print(0)
        exit(0)
    else:
        q.extend(check[count:count+length])    
        count+=length
print(1)

# print(result)





