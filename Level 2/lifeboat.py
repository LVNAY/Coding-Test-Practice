def solution(people, limit):
    answer = 0
    people.sort()
    rt = len(people) -1
    lt = 0
    while rt >= lt :
        if rt == lt :
            answer += 1
            break
        if people[rt] + people[lt] > limit :
            rt = rt - 1
            answer += 1
        else :
            lt = lt + 1
            rt = rt - 1
            answer += 1
    if len(people) == 1 :
        answer += 1
    
    return answer