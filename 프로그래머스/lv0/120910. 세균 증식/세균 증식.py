def solution(n, t):
    a = 1
    while a <= t:
        n *= 2
        a += 1
    answer = n
    return answer