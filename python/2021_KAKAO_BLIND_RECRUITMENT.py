def solution(new_id):
    # 1
    #print(new_id,end=' - >')
    new_id = new_id.lower() 
    #print(new_id)
    
    # 2
    #print(new_id,end=' - >')
    new_id = list(new_id)
    temp = []
    for i in new_id:
        if i.isdigit() or i.isalpha() or i=='-' or i=='_' or i=='.':
            temp.append(i)
    #print(temp)
    
    # 3
    count = 0
    new_id = []
    for i in temp:
        if i=='.':
            count +=1
            if count >1:
                continue
        else:
            count =0
        new_id.append(i)
    #print(new_id)
    # 4
    if len(new_id) > 0:    
        if new_id[-1]=='.' and len(new_id) >0:
            new_id = new_id[:-1]
    if len(new_id) > 0:    
        if new_id[0]=='.' and len(new_id) >0:
            new_id = new_id[1:]
    #print(*new_id,sep='')
    
    # 5
    if len(new_id)==0:
        new_id.append('a')
    
    # 6
    if len(new_id)>15:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]

    # 7
    if len(new_id) <3:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    
    answer = ''.join(new_id)
    print(answer)
    return answer


if __name__=='__main__':
    solution("...!@BaT#*..y.abcdefghijklm")
    solution('=.=')