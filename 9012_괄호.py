import sys

n = int(sys.stdin.readline())

for i in range(n):
    st = sys.stdin.readline().strip()
    stack = 0
    for k in st:
        if k == '(':
            stack +=1
        elif k == ')':
            stack -=1
        if stack < 0:
            break
    if stack == 0:
        print('YES')
    else:
        print('NO')