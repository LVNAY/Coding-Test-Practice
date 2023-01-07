import math

def solution(n,a,b):
    answer = 0

    x = math.log2(n)
    
    for i in range(0,int(x)) :
        a = (a+1)//2
        b = (b+1)//2
        i = i+1
        
        if a == b :
            answer = i
            break

    return answer