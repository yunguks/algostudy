'''
문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

예제 입력 1 
5457
3
6 7 8
예제 출력 1 
6
예제 입력 2 
100
5
0 1 2 3 4
예제 출력 2 
0
예제 입력 3 
500000
8
0 2 3 4 6 7 8 9
예제 출력 3 
11117
예제 입력 4 
100
3
1 0 5
예제 출력 4 
0
예제 입력 5 
14124
0
예제 출력 5 
5
예제 입력 6 
1
9
1 2 3 4 5 6 7 8 9
예제 출력 6 
2
예제 입력 7 
80000
2
8 9
예제 출력 7 
2228
'''
def rotation(input:str,n,check):
    global m
    global target
    global button
    if n<0:
        return check
    if input:
        # m 보다 작은수가 나온다면 check변경
        if m > (abs(target-int(input))+len(input)):
            m = (abs(target-int(input))+len(input))
            check = int(input)
    
    for i in button:
        # input에다가 새로운 i 붙이기
        temp = input+str(i)
        # 바뀐 check return
        check = rotation(temp,n-1,check)
    return check

import sys

input = sys.stdin.readline

target = input().rstrip()
len_target = len(target)
target = int(target)

n = int(input())
# 고장난게 없다면 바로 버튼 누르면됨
if n==0:
    print(min(abs(target-100),len_target))
    exit()
cut = list(map(int,input().split()))

# 모두가 고장 났다면 차이만큼 +-로 이동
if n==10:
    print(abs(100-target))
    exit()

# target이 100 현재와 같다면 아무것도 안눌러도 됨
if target ==100:
    print(0)
    exit()
button = [0,1,2,3,4,5,6,7,8,9]

# 고장난 버튼 제거
for i in cut:
    if i in button:
        button.remove(i)
#print(button)

# 초기 최솟값 설정 // 숫자 길이수 + 버튼 누른 횟수
m = abs(100-target)
# target의 자리수 만큼 for문 중첩 반복해서 찾기
# m 보다 작으면 return
num = rotation('',len_target+1,m)
# 자리수 + 남은차이를 +-로 이동
print(m)

'''
# 더 간단한 풀이 - 100000번 까지 돌아보고 그것이 고장난 버튼이 없으면 최소값 구하기
n = int(input())
m = int(input())
useless_buttons = list(input().strip())
result = abs(n - 100)

def is_exist(num):
    nums = list(str(num))
    for n in nums:
        if n in useless_buttons:
            return False
    return True

for i in range(1000001):
    if is_exist(i):
        result = min(result, len(str(i)) + abs(i - n))

print(result)
'''