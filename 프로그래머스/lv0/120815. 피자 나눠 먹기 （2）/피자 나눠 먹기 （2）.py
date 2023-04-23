def solution(n):
    n_list = [n]
    while True:
        if n_list[-1] % 6 != 0:
            n_list.append(n_list[-1] + n)
        else:
            break
    answer = n_list[-1] // 6
    return answer