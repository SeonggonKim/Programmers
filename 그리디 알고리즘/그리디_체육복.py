def solution(n, lost, reserve):
    answer = [1] * (n)
    for i in range(1, len(answer)+1):
        if i in reserve:
            answer[i-1] += 1
    for i in range(1, len(answer)+1):
        if i in lost:
            answer[i-1] -= 1
    for i in range(1, len(answer)):
        if answer[i-1] == 0 and answer[i] == 2:
            answer[i-1] += 1
            answer[i] -= 1
    for i in range(1, len(answer)):
        if answer[i-1] == 2 and answer[i] == 0:
            answer[i-1] -= 1
            answer[i] += 1
    cnt = 0
    for i in range(len(answer)):
        if answer[i] >=1:
            cnt += 1
    return cnt