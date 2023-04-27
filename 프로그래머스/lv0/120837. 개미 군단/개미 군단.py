def solution(hp):
    a = hp // 5
    least = hp - a*5
    b = least // 3
    least = least - b*3
    c = least // 1
    answer = a + b + c
    return answer