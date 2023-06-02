"""
문제
One of the most important data structures in computer science is the tree. You already dealt with binary trees in the qualification round. This problem is about general trees.

Trees are the subset of graphs that have the following 3 properties:

It is connected: for every node you can reach every other node following edges.
If an edge is removed, the graph is no longer connected. That is, some nodes cannot be reached anymore.
When an edge is added between two existing nodes A and B, a cycle is created. There is a cycle if there is more than one way to go from A to B.
Your task is to decide if a given graph is a tree or not.

입력
The first line will contain an integer T representing the number of graphs to check. There will be at most 10 graphs in each test case.

Each of the graph will be represented as follows:

The first line will contain an integer N with the number of nodes in the graph. The number of nodes will be between 1 and 1,000. The identifier of each node will be an integer from 1 to N. 

The next line will contain an integer M with the number of edges in the graph. There will be at most 106 edges.

The next M lines will contain 2 integers A and B each. These are the two nodes connected by an edge.

The total sum of M in all test cases is at most 106.

출력
For each graph, a single line with “tree” if the graph represents a tree or “graph“ otherwise.

예제 입력 1 
2
4
3
2 1
3 4
1 3
3
3
1 2
1 2
3 2
예제 출력 1 
tree
graph
예제 입력 2 
2
7
5
7 2
2 4
4 3
5 6
6 1
7
6
7 2
2 4
4 3
4 5
6 5
1 6
"""
import sys
from collections import deque

if __name__=="__main__":
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        num_node = int(sys.stdin.readline().rstrip())
        num_lines = int(sys.stdin.readline().rstrip())
        tree = [[] for _ in range(num_node+1)]

        # 1이면 트리
        flag = 1

        visit = [1]*(num_node+1)
        for _ in range(num_lines):
            a,b = map(int,sys.stdin.readline().split())
            tree[a].append(b)
            tree[b].append(a)

        # 동일한 노드 찾기
        for t in tree:
            if len(t)!=len(set(t)):
                flag = 0
                
        q= deque()
        visit[0] = 0
        visit[1] = 0
        for t in tree[1]:
            q.append([1,t])

        while len(q) and flag:
            before, next = q.pop()
            visit[next] = 0
            for t in tree[next]:
                if t != before:
                    if visit[t]:
                        q.append([next, t])
                    else:
                        flag =0
                        break
        if sum(visit):
            flag =0
        if flag:
            print("tree")
        else:
            print("graph")
