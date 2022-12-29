import sys

n = int(sys.stdin.readline())

output = [1]*1000001
output[0], output[1] = 0,0
# 처음 수는 소수가 아니라면 지워졌을 것이고
# 안지워졌다면 i*i 수 부터 확인하여 지운다.
# i*(i-1) 의 수는 i-1번째 에서 지웠을 것이기 때문이다
for i in range(2,int(1000000**0.5)+1):
    if output[i]==1:
        j = i
        while i*j < 1000001:
            output[i*j]=0
            j +=1

for _ in range(n):
    count = 0
    num = int(sys.stdin.readline())
    if output[num-2]==1:
        count+=1
    for i in range(3, num//2+1,2):
        if output[i]==1 and output[num-i]==1:
            count+=1
    print(count)
