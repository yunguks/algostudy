def solution(n, lost, reserve):
    l = [0 for _ in range(n+1)]
    r = [0 for _ in range(n+1)]

    for i in lost:
        l[i] = 1
    for j in reserve:
        r[j] = 1

    for i in range(n+1):
        if l[i]==1 and r[i]==1:
            l[i]=0
            r[i]=0
    
    for i in range(1,n):
        if l[i]==1:
            if r[i-1]==1:
                l[i]=0
                r[i-1]=0
                continue
            elif r[i+1]==1:
                l[i]=0
                r[i+1]=0

    answer = n-sum(l)
    return answer

if __name__=="__main__":
    n = 5
    lost = [2,4]
    reserve = [1,3,5]
    print(solution(n,lost,reserve))

    n = 5
    lost = [2,4]
    reserve = [3]
    print(solution(n,lost,reserve))

    n = 3
    lost = [3]
    reserve = [1]
    print(solution(n,lost,reserve))