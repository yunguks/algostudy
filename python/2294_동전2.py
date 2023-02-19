"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	128 MB	57417	17273	12133	29.241%
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 
그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 
각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 
다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 
동전의 가치는 100,000보다 작거나 같은 자연수이다. 
가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
3 15
1
5
12
예제 출력 1 
3
"""
import sys
import math
def info():
    n, k =map(int,sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
    return n,k,coins

def sol(n,k,coins):
    result = [0]*(k+1)

    result[0]=1
    for i in range(1,k+1):
        min_val = math.inf
        for c in coins:
            if i-c >= 0:
                if min_val > result[i-c] >0:
                    min_val= result[i-c]
        if min_val != math.inf:
            result[i]+=min_val+1
    
    if result[-1]==0:
        return -1
    else:
        return result[-1]-1
if __name__=="__main__":
    print(sol(*info()))
