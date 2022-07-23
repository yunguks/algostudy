import sys

n = int(sys.stdin.readline())

output = 1
for i in range(1,n+1):
    output *= i
print(output)