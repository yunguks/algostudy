import sys

back = []
front = []
total = []
for _ in range(int(sys.stdin.readline())):
    
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        front.append(int(command[1]))
    elif command[0] == 'push_back':
        back.append(int(command[1]))
    elif command[0] == 'pop_front':
        if front:
            print(front.pop())
        elif back:
            print(back.pop(0))
        else:
            print('-1')
    elif command[0] == 'pop_back':
        if back:
            print(back.pop())
        elif front:
            print(front.pop(0))
        else:
            print('-1')
    elif command[0] =='size':
        print(len(total))
    elif command[0] == 'empty':
        if total:
            print('0')
        else:
            print('1')
    elif command[0] == 'front':
        if total:
            print(total[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if total:
            print(total[-1])
        else:
            print('-1')
    total = []
    total.extend(reversed(front))
    total.extend(back)