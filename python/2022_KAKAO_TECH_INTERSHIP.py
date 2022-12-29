from collections import deque
import math
def solution(queue1, queue2):
    find = sum(queue1) + sum(queue2)
    if find%2!=0:
        return -1
    find = find//2

    c = 0
    max = len(queue1)*3
    queue1=deque(queue1)
    queue2=deque(queue2)
    s1 = sum(queue1)
    
    while queue1 and queue2:
        if c > max:
            return -1
        # q1에서 q2로 이동
        if s1>find:
            tmp = queue1.popleft()
            s1 -= tmp
            queue2.append(tmp)
            c +=1
        
        # q2에서 q1로 이동
        elif find > s1:
            tmp =queue2.popleft()
            s1 += tmp
            queue1.append(tmp)
            c +=1    
        else:
            return c
    return -1