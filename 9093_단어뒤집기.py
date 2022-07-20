import sys
n = int(sys.stdin.readline())

for i in range(n):
    st = sys.stdin.readline().strip()
    find = st.split()
    for j in find:
        for k in range(len(j)):
            k = k+1
            print(j[-k], end='')
        print(' ',end='')
    print()
        
