import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    def lcm(a, b):
        return a * b / math.gcd(a, b)
    b = lcm(denom1, denom2)
    numer1 = numer1 * (b // denom1)
    numer2 = numer2 * (b // denom2)
    a = numer1 + numer2
    c = math.gcd(int(a), int(b))
    a = a//c
    b = b//c
    answer.append(a)
    answer.append(b)
    return answer