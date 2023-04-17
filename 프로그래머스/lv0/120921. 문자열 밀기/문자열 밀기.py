def solution(A, B):
    answer = 0
    A_list = list(A)
    while True:
        if A == B:
            break
        elif answer > len(A_list):
            answer = -1
            break
        else:
            A_list.insert(0, A_list.pop())
            A = "".join(A_list)
            answer += 1
    return answer