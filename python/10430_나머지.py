import sys

n = sys.stdin.readline().rstrip().split()

n = list(map(int,n))

a=n[0]
b=n[1]
c=n[2]

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)* (b%c))%c)