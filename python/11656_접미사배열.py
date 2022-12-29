import sys

line = sys.stdin.readline().rstrip('\n')

output= []
for i in range(len(line)):
    output.append(line[i:])

print(*sorted(output),sep='\n')