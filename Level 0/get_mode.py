def solution(array):
    answer = ''
    lst = []
    a = sorted(list(set(array)))
    b = {}
    for i in a:
        b[i]=array.count(i)
    maxnum = max(b.values())
    for value, count in b.items():
        if count == max(b.values()):
            lst.append(str(value))
    if len(lst) > 1 :
        return -1
    else :
        return int(''.join(lst))