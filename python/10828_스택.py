import sys
# 이게 훨씬 빠르다.
n = int(sys.stdin.readline())
if n <1 and n>10000:
    exit()
stack = []
for i in range(n):
    st = sys.stdin.readline().strip()
    if st[:4]=='push':
        a, b = st.split( )
        stack.append(b)
    elif st == 'top':
        if len(stack)==0:
            print('-1')
        else:
            print(stack[-1])
    elif st == 'pop':
        if len(stack)==0:
            print('-1')
        else:
            print(stack.pop())
    elif st == 'size':
        print(len(stack))
    elif st =='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')
    