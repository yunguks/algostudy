import sys

a, b = map(int,sys.stdin.readline().split())

numbers = [1]*(b+1)
numbers[0], numbers[1] = 0, 0

for i in range(2,int(b**0.5)+1):
    if numbers[i]==1:
        # i*i 이전에는 앞에서 지웠음
        # 2의 배수는 앞에서 지우고 3의 배수 중에서 3,6,9,12 는 
        # 9부터 본다,
        # 4의 배수는 4 8 12 인데 4가 0이므로 보지 않는다.
        for j in range(i*i,b+1,i):
            numbers[j]=0

for i in range(a):
    numbers[i] = 0

for i in range(len(numbers)):
    if numbers[i]:
        print(i)
# def check(num):
#     for i in range(3, int(num*(0.5))+1,2):
#         if num%i==0:
#             return False
#     return True

# a, b = map(int,sys.stdin.readline().split())

# if a ==1:
#     print(2)
#     a=3
# if a%2 ==0:
#     a = a+1
# # 짝수는 확인 하지 않고
# for i in range(a, b+1,2):
#     if check(i):
#         print(i)
