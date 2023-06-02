"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	210	103	88	63.309%
문제
n개의 정점과 n - 1개의 간선으로 구성된 트리 T가 있다. 정점 번호는 0부터 n - 1까지이고 0번 정점이 루트이다. 간선에는 가중치가 없다. 트리 T에 있는 각 정점에는 서로 다른 값이 부여된다. 트리 T에서 정점에 부여된 값이 k인 노드의 깊이(depth)를 출력하자. 루트 정점의 깊이는 0이고 자식 정점의 깊이는 부모 정점의 깊이보다 1만큼 더 큰 값을 갖는다.

입력
첫 번째 줄에 정점의 수 n과 정수 k가 공백을 사이에 두고 순서대로 주어진다.

두 번째 줄부터 n - 1개 줄에 걸쳐 간선의 정보가 주어진다. 한 줄에 하나의 간선 정보가 주어진다. 하나의 간선 정보는 부모 정점 번호 p와 자식 정점 번호 c가 공백을 사이에 두고 순서대로 주어진다.

다음 줄에는 0번 정점부터 n - 1번 정점까지 각 정점에 부여된 값이 공백을 사이에 두고 순서대로 주어진다. 즉, i번째 수는 i - 1번 정점에 부여된 값을 의미한다.

출력
첫 번째 줄에 정점에 부여된 값이 k인 정점의 깊이를 출력한다.

제한
2 ≤ n ≤ 100,000
0 ≤ k ≤ n - 1
0 ≤ p, c ≤ n - 1, p ≠ c
간선들로 만들어진 그래프는 트리이다.
0 ≤ 정점에 부여된 값 ≤ n - 1
각 정점에 부여된 값은 서로 다른 정수이다.
예제 입력 1 
8 5
0 1
0 2
1 3
1 4
2 5
2 6
6 7
0 1 2 3 4 5 6 7
예제 출력 1 
2
"""
import sys
if __name__=="__main__":
    N, K = map(int,sys.stdin.readline().split())
    union = [i for i in range(N)]
    for _ in range(N-1):
        p, c = map(int,sys.stdin.readline().split())
        union[c]=p
    
    values = list(map(int,sys.stdin.readline().split()))
    
    target = 0
    for i in range(len(values)):
        if values[i]==K:
            target = i
            break
    depth = 0
    while target!=union[target]:
        depth+=1
        target = union[target]
    
    print(depth)