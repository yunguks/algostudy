import sys

a, b= sys.stdin.readline().split()
b = int(b)
result = 0
k =1
for i in reversed(range(0,len(a))):
    if ord(a[i]) < 60:
        num = int(a[i])
    else:
        num = ord(a[i])-55
    result += num*k
    k *=b
print(result)