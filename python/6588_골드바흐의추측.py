import sys

numbers= [0,1]*500001
for i in range(3,int(1000000**(0.5))+1,2):
    if numbers[i]==1:
        numbers[i]==0
        j = i
        while i*j<1000001:
            numbers[i*j]=0
            j +=1
numbers[1]=0

while True:
    n = int(sys.stdin.readline())
    if n ==0:
        break
    # print(f'n = {n}')
    for i in range(3,n//2+1,2):
        if numbers[i]==1:
            if numbers[n-i]==1:
                print(f'{n} = {i} + {n-i}')
                break
    