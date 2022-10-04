def solution(board, moves):
    
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                pop = board[j][i-1]
                board[j][i-1] = 0
                if stack:
                    if stack[-1]==pop:
                        answer +=2
                        stack.pop()
                    else:
                        stack.append(pop)
                else:
                    stack.append(pop)
                break

    return answer

if __name__=='__main__':
    b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    m = [1,5,3,5,1,2,1,4]
    print(solution(b,m))