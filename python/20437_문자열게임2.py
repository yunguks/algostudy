"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	3329	1433	1055	41.308%
문제
작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

알파벳 소문자로 이루어진 문자열 W가 주어진다.
양의 정수 K가 주어진다.
어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
위와 같은 방식으로 게임을 T회 진행한다.

입력
문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)

다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) 

출력
T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.

만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.

예제 입력 1 
2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5
예제 출력 1 
4 8
-1
첫 번째 문자열에서 3번에서 구한 문자열은 aqua, 4번에서 구한 문자열은 raquator이다.

두 번째 문자열에서는 어떤 문자가 5개 포함된 문자열을 찾을 수 없으므로 -1을 출력한다.

예제 입력 2 
1
abaaaba
3
예제 출력 2 
3 4
"""
import sys
import math
from collections import defaultdict

if __name__=="__main__":
    N = int(sys.stdin.readline().rstrip())
    
    for _ in range(N):
        string = list(sys.stdin.readline().rstrip())
        K = int(sys.stdin.readline().rstrip())
        length = len(string)
        m = math.inf
        M = -1
        
        counter = defaultdict(list)

        for i in range(len(string)):
            counter[string[i]].append(i)

        for value in counter.values():
            if len(value) < K:
                continue
            for i in range(len(value)-K+1):
                m = min(m,value[i+K-1]-value[i]+1)
                M = max(M,value[i+K-1]-value[i]+1)

        if M == -1:
            print(-1)
        else:
            print(m,M)

        # info = Counter(string)
        # for s, c in info.most_common():
        #     if c < K:
        #         break
        #     checklist.append(s)

        # for i in range(len(string)):
        #     if string[i] not in checklist:
        #         continue

        #     s = string[i]
        #     count = 1
            
        #     for j in range(i+1,len(string)):
        #         # print(f"{string[j]} , {m,M}")
        #         if string[j]==s:
        #             count +=1
        #             if count == K:
        #                 m = min(m,j-i+1)
        #                 M = max(M,j-i+1)
        #                 break
        #     # print(f"{i} {s} {m} {M}")    