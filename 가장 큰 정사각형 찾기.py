def solution(board):
    length_x = len(board)
    length_y = len(board[0])
    if length_x ==1 or length_y==1:
        return 1
    visit=[[0 for _ in range(length_y)] for _ in range(length_x)]
    max =0
    for x in range(1,length_x):

        for y in range(1,length_y):
            if board[x][y]!=0:
                m = min(board[x-1][y],board[x][y-1],board[x-1][y-1]) +1
                board[x][y] = m
                
                if m > max:
                    max = m

    answer = max**2
    return answer