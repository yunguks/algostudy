import sys

def cal(x):
    count = [0]*(x+1)
    if x==1:
        return 0
    count[2] = 1

    for i in range(3,x+1):
        temp = count[i-1]
        if i%3==0:
            if temp > count[i//3]:
                temp = count[i//3]
        if i%2==0:
            if temp > count[i//2]:
                temp = count[i//2]
        
        count[i]=temp+1

    return count[x]

n = int(sys.stdin.readline())

print(cal(n))