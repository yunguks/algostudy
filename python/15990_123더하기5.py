'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

1+2+1
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
3
9
27
'''
import sys
# [1로 끝나는 경우의 수 , 2로 끝나는 경우의 수, 3으로 끝나는 경우의 수]
# output[i]에 넣어서 output[i-1]은 1로 끝나는 경우의 수를 보지 않는다.

n=int(sys.stdin.readline())
output =[[0 for j in range(3)] for i in range(100000+1)]
output[1]=[1,0,0]
output[2]=[0,1,0]
output[3]=[1,1,1]

# 이 계산을 밑에 for문에 넣으니 시간초과
# 배열이 비어있어도 nxk번(최대 T*100000) 만큼 보니까
# 한번에 모두 계산해 놓으면 100000 만 한다
for i in range(4,100001):
    # i-1번째에서 1로 끝나는 개수 빼고
    output[i][0]+=(output[i-1][1]+output[i-1][2])%1000000009
    # i-2번째에서 2로 끝나는 개수 빼고
    output[i][1]+=(output[i-2][0]+output[i-2][2])%1000000009
    # i-3번째에서 3으로 끝나는 개수 빼고
    output[i][2]+=(output[i-3][0]+output[i-3][1])%1000000009

for _ in range(n):
    k = int(sys.stdin.readline())

    print(sum(output[k])%1000000009)

'''
모든 덧셈 순서를 저장해서 시간초과가 뜸
def check(n):
    global output
    for i in range(4,n+1):
        temp = []
        if not output[i]:
            for a in output[i-1]:
                if a[-1]!=1:
                    temp.append(a+[1])
            for b in output[i-2]:
                if b[-1]!=2:
                    temp.append(b+[2])
            for c in output[i-3]:
                if c[-1]!=3:
                    temp.append(c+[3])

        output[i].extend(temp)
    return len(output[n])

n = int(sys.stdin.readline())

output=[[] for i in range(100000)]
output[1].append([1])
output[2].append([2])
output[3].extend([[3],[1,2],[2,1]])

for _ in range(n):
    k = int(sys.stdin.readline())
 
    print(check(k))

'''
    