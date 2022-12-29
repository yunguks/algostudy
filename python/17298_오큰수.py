import sys

n = int(sys.stdin.readline())
words = list(map(int,sys.stdin.readline().rstrip().split()))
stack = []
output = [-1 for i in range(n)]
# 뒤에 있는 수열이 작은 것은 볼 필요가 없다
# 큰 수들을 하나씩 stack에 넣어서 top
for i in range(n-1,-1,-1):
    while stack:
        if words[i] < stack[-1]:
            output[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(words[i])
    
print(*output,sep=' ')

'''
# 시간 초과 문제 
n = int(sys.stdin.readline())
words = list(map(int,sys.stdin.readline().rstrip().split()))
output = [-1 for i in range(n)]

for i in range(len(words)):
    for j in range(i):
        if output[j] == -1:
            if words[j] < words[i]:
                output[j] = words[i]

print(*output,sep=' ')
'''

