"""
하지만 햄스터의 부피는 
$M$으로 정해져 있기 때문에, 늘릴 수 있는 크기에는 한계가 있다.

독에 왼쪽부터 
$N$개의 구멍이 일렬로 뚫려 있고, 
$i$번째 구멍의 크기 
$A_i$가 주어진다. 햄스터는 구멍을 막기 위해 정확히 그 크기만큼의 부피를 소모해야 한다.

싫은데요 햄스터는 콩쥐에게 최대한 도움이 되길 원하기 때문에 자기 부피를 가능한 한 많이 활용하길 원한다.

어떻게 막으면 햄스터가 원하는 방식으로 독을 막는지 구해서 알려주자.

아무리 햄스터가 유체라고 하지만 몸을 둘로 나눌 수는 없기 때문에 막는 모든 구멍은 연속되어야 한다.

입력
입력은 아래와 같이 주어진다.


출력
구멍을 막는 데에 활용할 수 있는 최대 부피를 출력한다.

예제 입력 1 
8 10
2 2 2 2 11 2 5 2
예제 출력 1 
9
"""

import sys

if __name__=="__main__":
    N,M = map(int,sys.stdin.readline().split())
    As = list(map(int,sys.stdin.readline().split()))
    left =0
    right = 0
    max_value = 0
    ham = 0
    while right < N:
        if ham <= M:
            max_value = max(max_value,ham)
            ham+= As[right]
            right+=1
        else:
            ham-= As[left]
            left+=1
    if ham <= M:
        max_value = max(max_value,ham) 
    print(max_value)

