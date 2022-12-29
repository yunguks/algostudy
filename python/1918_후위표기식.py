import sys

cal = sys.stdin.readline().rstrip()

stack = []
output = []
order = {'+':1,'-':1,'*':2,'/':2,'(':0}

for i in cal:
    if i.isalpha():
        output.append(i)
    else:
        if stack!=[]:
            if i ==')':
                while stack:
                    if stack[-1]!='(':
                        output.append(stack.pop())
                    else:
                        stack.pop()
                        break

            elif i=='(':
                stack.append(i)
            else :
                while stack:
                    if order[i] > order[stack[-1]]:
                        break
                    output.append(stack.pop())
                stack.append(i)
        else:
            stack.append(i)
while stack:
    output.append(stack.pop())

print(*output,sep='')

