import sys

line = sys.stdin.readline().rstrip('\n')

line = line.split()

# line[0] = line[0]+line[1]
# line[1] = line[2]+line[3]
# print(int(line[0])+int(line[1]))

a = int(line[0]+line[1])
b = int(line[2]+line[3])

print(a+b)
