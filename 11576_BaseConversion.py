import sys

a, b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

line = list(map(int,sys.stdin.readline().split()))
num = 0
k = 1
for i in reversed(range(n)):
    num += line[i]*k
    k *= a

output = []
while num>0:
    output.append(num%b)
    num = num//b
print(*reversed(output))

