"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	1069	400	285	37.206%
문제
n개의 자연수로 이루어진 수열이 주어질 때, 특정 구간 [i,j](i≤j)의 합이 k보다 큰 모든 쌍 i,j의 개수를 출력하시오.

입력
첫째 줄에는 숫자들의 개수 n이 주어진다(1≤n≤100,000)

다음 줄에는 숫자 n개가 주어진다. 숫자들은 100,000보다 크지 않은 자연수임이 보장된다.

그 다음 줄에는 숫자 k가 주어진다. (1≤k≤1,000,000,000)

출력
특정 구간 [i,j]의 합이 k보다 큰 모든 쌍 i,j의 개수를 출력하시오.

예제 입력 1 
5
1 2 3 2 1
7
예제 출력 1 
3
예제 입력 2 
5
1 1 1 1 1
2
예제 출력 2 
6
"""
import sys
from collections import deque
if __name__=="__main__":
    N = int(sys.stdin.readline().rstrip())
    strings = list(map(int,sys.stdin.readline().split()))
    K = int(sys.stdin.readline().rstrip())
    
    start = 0
    end = -1
    count = 0
    S = 0
    while True:
        if S <= K:
            end +=1
            if end == N:
                break
            S += strings[end]
        else:
            S -= strings[start]
            count += (N-end)
            start+=1
    print(count)
            
            
        
    