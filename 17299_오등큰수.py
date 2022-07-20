import sys

n = int(sys.stdin.readline().rstrip())
words = sys.stdin.readline().rstrip().split()
count = {}
output = [-1]*n

for i in range(n):
    if not words[i] in count.keys():
        count[words[i]] = 1
    else:
        count[words[i]] += 1

stack = []

# stack에 두가지 리스트 넣기
for i in range(n-1,-1,-1):
    while stack:
        if count[words[i]] < stack[-1][1]:
            output[i] = stack[-1][0]
            break
        else:
            stack.pop()

    stack.append([words[i], count[words[i]]])
print(*output,sep=' ')

'''
딕셔너리가 더 느림
for i in range(n-1,-1,-1):
    while stack:
        temp = stack[-1]
        if count[words[i]] < list(temp.values())[0]:
            output[i] = list(temp.keys())[0]
            break
        else:
            stack.pop()
    stack.append({words[i]:count[words[i]]})
print(*output,sep=' ')
'''