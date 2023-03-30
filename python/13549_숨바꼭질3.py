"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	65453	18805	12123	25.216%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이
 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
2
"""
import sys
import heapq
if __name__=="__main__":
    N,K = map(int,sys.stdin.readline().split())
    result = K
    max_val = max(min(2*K,100000),N)
    visit = [0 for _ in range(max_val+1)]
    q = []
    visit[N]=1
    heapq.heappush(q,[0,N])
    while len(q) > 0:
        time,x = heapq.heappop(q)
        if x ==K:
            result = time
            break
        if 0< 2*x <=max_val and visit[2*x]==0:
            visit[2*x]==1
            heapq.heappush(q,[time,2*x])
        for new_x in (x+1,x-1):
            if 0 <= new_x <=max_val and visit[new_x]==0:
                visit[new_x]=1
                heapq.heappush(q,[time+1,new_x])

    print(result)