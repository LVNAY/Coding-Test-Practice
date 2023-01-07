def solution(n):
    answer = 0
    convert = ''
    while n > 0:
        n, mod = divmod(n, 3)
        convert += str(mod)
    answer = int(convert, 3)
    return answer