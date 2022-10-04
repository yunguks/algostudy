def solution(numbers, hand):
    def distance(target, l, r, bias):
        if target ==0:
            x,y = 3,1
        else:
            x = (target-1)//3
            y = (target-1)%3
        if bias =='right':
            bias = 'R'
        else:
            bias = 'L'
    
        if abs(l[0]-x) + abs(l[1]-y) > abs(r[0]-x) + abs(r[1]-y):
            return [x,y],'R'
        elif abs(l[0]-x) + abs(l[1]-y) < abs(r[0]-x) + abs(r[1]-y):
            return [x,y],'L'
        else:
            return [x,y],bias

    stack = []

    left = [3,0]
    right = [3,2]
    
    for i in numbers:
        # print(f' {i} -> {stack}')
        # print(f'left : {left}, right : {right}')
        if i in [1,4,7]:
            stack.append('L')
            left = [i//3 ,0]
        elif i in [3,6,9]:
            stack.append('R')
            right = [(i-1)//3,2] 
        else:
            position , h = distance(i,left,right,hand)
            stack.append(h)
            if h =='R':
                right = position
            else:
                left = position
    
    answer = ''.join(stack)
    return answer

if __name__=='__main__':
    n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    h = "right"
    print(solution(n,h))

    n = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    h = "left"
    print(solution(n,h))

    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    h = "right"
    print(solution(n,h))