import sys
import string
alpha = list(string.ascii_lowercase)

output ={}
for i in alpha:
    output[i]= 0
# for i in range(len(alpha)):
#     output[alpha[i]] = 0

line = sys.stdin.readline().rstrip()

for i in line:
    output[i] +=1

print(*list(output.values()),sep=' ')