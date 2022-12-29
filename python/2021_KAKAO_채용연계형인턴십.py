from collections import deque
import heapq
from heapq import heappop, heappush
def solution(places):
    
    def check(maps,position):
        map = maps[:]
        # [x,y,2-distance]
        # [p의 좌표 입력]

        plan = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in position:
            q = []
            visit = [[0 for _ in range(5)] for _ in range(5)]
            q.append([0,i[0],i[1]])
            find=0
            while len(q):
                dis,x,y = heappop(q)
                visit[x][y]=1
                for p in plan:
                    new_x = x+p[0]
                    new_y = y+p[1]
                    if -1<new_x<5 and -1<new_y<5 and visit[new_x][new_y]==0:
                        new_s = map[new_x][new_y]
                        if new_s=='X':
                            heappush(q,[dis+2,new_x,new_y])
                        elif new_s =='O':
                            heappush(q,[dis+1,new_x,new_y])
                        elif new_s=='P':
                            if dis < 2:
                                return 0
                            else:
                                find=1
                                break
                if find==1:
                    break
        return 1
    answer = []
    for i in range(len(places)):
        position = []
        for j in range(len(places[0])):
            for k in range(len(places[0])):
                if places[i][j][k] == 'P':
                    position.append([j,k])
        
        answer.append(check(places[i],position))

    print(answer)
    return answer

if __name__=='__main__':
    solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])