def solution(sides):
    if sum(sides) > max(sides)*2:
        answer = 1
    else:
        answer = 2
    return answer