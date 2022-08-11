'''
문제
1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
1 2 4 3
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
-1
'''

import sys

input = sys.stdin.readline
N = int(input())
ans = list(map(int,input().split()))

# 뒤에서 부터 i < i+1 일때 바꾼다.
for i in range(N-2,-1,-1):
    # 바뀌는 부분 i를 찾고 i보다 큰 수가 있다면 뒤에서 부터 있따면 바꾼다.
    # 왜? i 부터 그후는 내림 차순 정렬 되 어 있을 것이므로
    # 뒤에서 부터 큰 것이 나올 때 바꾼다면 , i수 다음 번 으로 큰 수 일 것이기 때문 
    if ans[i] < ans[i+1]:
        for j in range(N-1,i,-1):
            if ans[i] < ans[j]:
                ans[i],ans[j] = ans[j], ans[i]
                # 바꾸고 나머지는 정렬
                ans[i+1:] = sorted(ans[i+1:])
                print(*ans)
                exit()
print(-1)

'''
틀린 풀이
check = -1
# 맨 뒤 수보다 작은 수가 나올 때 까지
for i in range(N-2,-1,-1):
    if ans[i] < ans[-1]:
        check = i
        break
# 맨 뒤의 수보다 작은 것도 나을 수 있으나,
# 
# 맨 뒤보다 작은 수 그 뒤 수에서 비교한다.
# 모든 수가 내림차순이라면 맨 뒤와 check를 바꾸고
# 아니라면 오름 차순이 되는 순간의 수랑 바꾼다.
temp = check
for i in range(N-2,check,-1):
    if ans[i] < ans[i+1]:
        temp= i
        break

if temp==-1:
    print(-1)
    exit()

elif temp==check:
    ans[check], ans[-1] = ans[-1], ans[check]
else:
    ans[temp], ans[temp+1] = ans[temp+1], ans[temp]

# 작은 수가 나온 i-1번 째 수랑 i번쨰 수랑 바꾸고
# 나머지 수는 정렬한다.
ans[temp+1:]=sorted(ans[temp+1:])
print(*ans) 
'''