import sys
import math
n, s = map(int,sys.stdin.readline().split())

# 모든 거리가 최대 공약수를 공유해야 한다.
people = list(map(int,sys.stdin.readline().split()))

for i in range(len(people)):
    people[i] = abs(people[i]-s)

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b!=0:
        temp = a
        a = b
        b = temp%b
    return a

# 먼저 gcd를 구하고 그 구한 gcd를 다음 것과 계산한다.
# 만약 이전에 구한 gcd보다 작다면 업데이트 아니라면 
# 유지 될 것이다. 어떠한 값으로 시작해도 상관없다.
for i in people:
    people[0] = gcd(i,people[0])
print(people[0])

'''
print(math.gcd(*people))
'''    
