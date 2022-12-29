import sys

while True:
    output = [0]*4
    # \n만 제거하여서
    line = sys.stdin.readline().rstrip('\n')

    # 받은 문장이 없다면 종료
    if not line:
        break
    for i in line:
        if i.islower():
            output[0] +=1
        elif i.isupper():
            output[1] +=1
        elif i.isnumeric():
            output[2] +=1
        elif i==' ':
            output[3] +=1
        else:
            break
    print(*output,sep=' ')