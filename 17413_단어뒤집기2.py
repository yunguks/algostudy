import sys

words = sys.stdin.readline().rstrip()

tag1 = []
tag2 = []
check = 1
point = 0

for i in range(len(words)):
    if words[i]=='<':
        check = 0
        tag2.extend(list(reversed(tag1)))
        tag1 = []

    if check:
        if words[i]==' ':
            
            tag2.extend(list(reversed(tag1)))
            tag2.append(' ')
            tag1 = []
        else:
            tag1.append(words[i])
    else:
        tag2.append(words[i])
    
    if words[i] =='>':
        check = 1
if tag1:
    tag2.extend(list(reversed(tag1)))
print(*tag2,sep='')