import sys

n = int(sys.stdin.readline())

# 소인수 list를 만들 필요가 x
# check = [1]*(n+1)
# check[0], check[1]=0,0
# for i in range(2,int(n**0.5)+1):
#     if check[i] == 1:
#         j = i
#         while i*j < n+1:
#             check[i*j]=0
#             j +=1

for i in range(2,n//2+1):
    while n%i==0:
        n = n//i
        print(i)
    if n ==1:
        break
if n!=1:
    print(n)