import sys

lines = sys.stdin.readline().rstrip()

count = 0
bar = 0
total = 0
for i in range(len(lines)):
    if lines[i]=="(":
        if lines[i+1]==")":
            total += bar
        else:
            bar +=1

    else:
        if lines[i-1]!='(':
            bar -= 1
            total +=1
        
print(total)