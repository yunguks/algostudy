import sys

n,k = map(int,sys.stdin.readline().split())

man= [i+1 for i in range(n)]
count = 0
total = 0

print('<',end='')
for i in range(n):
    total +=k
    total -=1
    total= total%len(man)
    
    print(f'{man.pop(total)}',end='')
    
    if i!=n-1:
        print(', ',end='')

print('>')

