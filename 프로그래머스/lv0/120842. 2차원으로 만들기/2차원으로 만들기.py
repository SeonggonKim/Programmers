def solution(num_list, n):
    answer = [[] for _ in range(len(num_list)//n)]
    i, j = 0, 0
        
    while True:
        if i == len(answer):
            break
        elif len(answer[i]) != n:
            answer[i].append(num_list[j])
            j += 1
        else:
            i += 1
            
    return answer