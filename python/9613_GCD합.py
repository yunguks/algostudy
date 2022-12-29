import sys
import math

n = int(sys.stdin.readline())

def gcd(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a 

for _ in range(n):
    num = list(map(int,sys.stdin.readline().split()))

    output = 0 

    for i in range(1,num[0]):
        for j in range(i+1,num[0]+1):
            k = gcd(num[i],num[j])
            output = output + k 

    print(output)