import sys

n = int(sys.stdin.readline())
lines = list(map(int,sys.stdin.readline().split()))

def check(a):
    num = 1
    for i in range(2,int(a**(0.5))+1):
        if a%i == 0:
            num= i
    if num ==1:
        return True
    else:
        return False
        
count =0
for num in lines:
    if num >1:
        if check(num):
            count +=1
print(count)
