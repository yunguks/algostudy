import sys

n = sys.stdin.readline()
# 10진법으로 변경
n = int(n,2)
#print(n)
# 8진법으로 변경
n = oct(n)[2:]
print(n)

'''
내장함수 사용하지 않고 푸니 틀렸다고 나옴
line = list(sys.stdin.readline().rstrip())
line = list(map(int,line))

a = len(line)%3
if a==1:
    print(line[0])
elif a==2:
    print(line[0]*2+line[1],end='')

for i in range(a,len(line),3):
    print(line[i]*4+line[i+1]*2+line[i+2],end='')
'''