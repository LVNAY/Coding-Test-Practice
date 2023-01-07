def solution(n):
    answer = n
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        for i in range(int(n/2)+1):
            if n % (i+1) == 0 :
                print(i+1)
                answer += (i+1)
    return answer