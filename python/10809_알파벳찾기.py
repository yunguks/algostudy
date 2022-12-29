import sys
import string

alpha = list(string.ascii_lowercase)

output = {}
for i in alpha:
    output[i]=-1

line = sys.stdin.readline().rstrip()

for i in range(len(line)):
    if output[line[i]]==-1:
        output[line[i]]=i

print(*list(output.values()),sep=' ')