def solution(k, tangerine):
    answer = 0
    count = []
    dic = {}
    count = []
    for i in tangerine:
        dic[i] = dic.get(i, 0)
        dic[i] += 1
    for value in dic.values() :
        count.append(value)
    count.sort(reverse = True)
    sum = 0
    for j in count :
        sum += j
        answer += 1
        if sum >= k :
            break
    return answer