import sys
import math

n = sys.stdin.readline().rstrip()
a, b = map(int,n.split())

# print(math.gcd(a,b))
# print(math.lcm(a,b))

# a가 더 큰수로
if a <b:
    a,b = b,a
# 최대 공약수
k = 1    
for i in range(b,0,-1):
    print(i)
    if a%i==0 and b%i==0:
        k = i     
       # break   
print(k)

# 최소 공배수
print((a*b)//k)