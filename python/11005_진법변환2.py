import sys

n, k = map(int,sys.stdin.readline().split())

output=[]

while n:
    temp = n%k
    n = n//k
    if temp >9:
        output.append(chr(temp+55))
    else:
        output.append(temp)
print(*reversed(output),sep='')