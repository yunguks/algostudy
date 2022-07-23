import sys

n = int(sys.stdin.readline())

count = 0
k = 1
for i in range(1,n+1):
    k *=i
while True:
    if k%10==0:
        count+=1
        k = k//10
    else:
        break

print(count)