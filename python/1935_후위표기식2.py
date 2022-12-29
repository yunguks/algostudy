import sys

n = int(sys.stdin.readline())
cal = sys.stdin.readline().rstrip()

stack = []
num = 0
numbers = {}
for i in range(len(cal)):

    if cal[i] == "+":
        num = stack.pop()
        num = num + stack.pop()
    elif cal[i] == '-':
        num = stack.pop()
        num = stack.pop() - num
    elif cal[i] == '*':
        num = stack.pop()
        num = num * stack.pop()
    elif cal[i] == '/':
        num = stack.pop()    
        num =  stack.pop() / num
    else:
        if not cal[i] in numbers:
            num = int(sys.stdin.readline())
            numbers[cal[i]] = num
        num = numbers[cal[i]]
    stack.append(num)
print(f'{num:.2f}')
    


    
    