import sys
import math
n = int(sys.stdin.readline())

# 몫의 값이 1,0 이 되도록 계속해서 반복하고
# 나머지값들을 추출하면 된다.
# ** 항상 나머지 값들이 양수가 되도록
# print(math.ceil(-13/-2),math.floor(-13/-2)) # 7, 6 나머지는 +1, -1
# print(math.ceil(13/-2),math.floor(13/-2)) # -6, -7 나머지는 +1, -1
# print(13%-2, -13%-2, 14%-2, -14%-2) # -1 -1 0 0
# print(13//-2, -13//-2, -1//-2, 1//-2) # -7 6 0 -1

output = []
if n ==0:
    output.append(0)

while n:
    if n%-2:
        n = n//-2 +1
        output.append(1)
    else:
        n = n//-2
        output.append(0)
print(*reversed(output),sep='')
'''
시간 초과 풀이
a, b= 0, 0 
output = []
k = -2
while not (0<a<abs(k)):
    a = math.ceil(n/k)
    b = n-a*k
    n= a
    output.append(b)
output.append(a)
print(*reversed(output),sep='')

'''
