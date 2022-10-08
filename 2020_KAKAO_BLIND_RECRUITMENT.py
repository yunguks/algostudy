def solution(s):
    if len(s)<3:
        return len(s)
    # 연속으로 중복되는 것이 있는지 확인
    result = []
    k =1
    while k < (len(s)//2+1):
        count = len(s)
        temp = s[0:k]
        c = 1
        for i in range(k,len(s),k):
            if temp == s[i:i+k]:
                c +=1
                count = count- k
            else:
                temp = s[i:i+k]
                if c>1:
                    count +=len(str(c))
                    c=1
        
        if c>1:
            count +=len(str(c))
            
        result.append(count)
        k +=1
    answer = min(result)
    return answer