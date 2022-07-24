import sys

n = sys.stdin.readline()
# 10진법으로 변경
n = int(n,8)
# 2진법으로 변경
out = format(n,'b')
print(out)