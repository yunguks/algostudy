import sys

# left가 커서 왼쪽, right 가 커서 오른쪽을 거꾸로 한 것으로 
# insert와 remove를 사용하면 시간이 오래걸림
# pop과 append 를 이용하여 푼다.
left = list(sys.stdin.readline().rstrip())
right = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])
print(*(left+right[::-1]),sep='')
#print(*(left+list(reversed(right))),sep='')
''' 시간초과
sentence = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())

cursor = len(sentence)
for i in range(n):
    input = sys.stdin.readline().strip()

    if input=='L':
        if cursor !=0:
            cursor -=1
    elif input=='D':
        if cursor !=len(sentence):
            cursor +=1
    elif input=='B':
        if cursor !=0:
            del sentence[cursor-1]
            cursor -=1
    elif input[0]=='P':
        p, word = input.split()
        sentence.insert(cursor,word)
        cursor+=
        
print(*sentence,sep='')
'''
    
