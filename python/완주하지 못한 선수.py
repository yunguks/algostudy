def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)

    while c:
        if p[-1]==c[-1]:
            p.pop()
            c.pop()
        else:
            answer=p.pop()
            return answer
    answer = p.pop()
    return answer

if __name__=='__main__':
    p = ["leo", "kiki", "eden"]
    c = ["eden", "kiki"]
    print(solution(p,c))

    p = ["marina", "josipa", "nikola", "vinko", "filipa"]
    c = ["josipa", "filipa", "marina", "nikola"]
    print(solution(p,c))

    p = ["mislav", "stanko", "mislav", "ana"]
    c = ["stanko", "ana", "mislav"]
    print(solution(p,c))