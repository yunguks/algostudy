import sys

n, m= map(int,sys.stdin.readline().split())

count2 =0
count5 =0

# 2로 나누면 2의 배수가 몇개 인지 나오고
# 4로 나누면 4의 배수가 몇개 인지 나온다. 그러면 2의 개수가 카운트 된다
def cal(k,num):
    i =k
    c = 0
    while i <=num:
        c += num//i
        i = i*k
    return c
# m! 과 n-m*~*n 까지만 하려 했으나 그럴경우 1부터 시작하지 않아서
# 단순히 나누기로만 2의 배수가 몇개 5의 배수가 몇개인지 알 수 없다.

count2 = cal(2,n)-cal(2,m)-cal(2,n-m)
count5 = cal(5,n)-cal(5,m)-cal(5,n-m)

print(min(count2,count5))

'''
시간 초과
def factorial(a):
    k=1 
    for i in range(1,a+1):
        k *=i
    return k

a, b = map(int,sys.stdin.readline().split())

count =0
num = factorial(a)/factorial(b)/factorial(a-b)

while num%10==0:
    count+=1
    num = num//10

print(count)
'''