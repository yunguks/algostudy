from collections import deque
def solution(n, info):
    
    def cal(a_list,b_list):
        a = 0
        b = 0
        for i in range(len(a_list)):
            if a_list[i] < b_list[i]:
                b += 10-i
            else:
                if a_list[i]>0:
                    a+=10-i
        return b-a

    my_info = [0]*len(info)

    max = 0

    answer= [0]*len(info)
    q = deque()
    q.append([my_info,0])
    while q:
        state, i = q.pop()
        if i==len(info) or n==sum(state):
            m = cal(info,state)
            if max <= m:
                max = m
                answer = state
            continue
                
        q.append([state ,i+1])
        if n - sum(state)-(info[i]+1) > -1:
            new_info = state[:]
            new_info[i] = info[i]+1
            q.append([new_info, i+1])
        

    if n > sum(answer):
        answer[-1] += n-sum(answer)
    if max >0:
        return answer
    else:
        return [-1]

    # def shot(count, my_info, k, s):
        # if k ==10:
        #     m = s-a_score
        #     if max < m:
        #         max = m
        #         answer = my_info
        #         return 1
        #     else:
        #         return 0

        # if count-info[k]<0:
        #     shot(count,my_info,k+1,s)
        # else:
        #     new_info = my_info[:]
        #     new_info[k] = info[k]+1
        #     n_s = s+10-k
    #     #     shot(count-info[k],new_info,k+1,n_s)
    # if shot(n,my_info,0, 0):
    #     return answer
    # else:
    #     return [-1]

if __name__=='__main__':
    print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
    print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
    print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
    print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))

# def solution(n, info):
#     print(n)
#     count = n
#     price = []
#     a_score = 0
#     for i in range(len(info)):
#         if info[i] >0:
#             a_score += (10-i)
#             # 어피치가 쏜 화살의 점수를 뺏는다면 기대값*2
#             # 화살 한개당 기댓값 계산 [기대값, 화살수, i번째]
#             price.append([2*(10-i)/(info[i]+1),info[i]+1,i]) 
#         else:
#             price.append([10-i,1,i]) 

#     price = sorted(price,reverse=True)
#     print(price)
#     answer = [0]*len(info)
#     my_score =0
#     for i in range(len(price)):
#         if count - price[i][1] <0:
#             continue
#         count -=price[i][1]
#         answer[price[i][2]] = price[i][1]
#         my_score += price[i][1]*(10-price[i][2])
    
#     if count >0:
#         answer[-1] +=count
#     if my_score > a_score:
#         return answer
#     else:
#         return [-1]