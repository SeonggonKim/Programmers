def solution(num_list):
    answer = []
    for _ in range(len(num_list)):
        answer.append(num_list.pop())
    return answer