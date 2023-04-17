def solution(n):
    answer = ''
    my_dict = {0:'수', 1:'박'}
    for i in range(n):
        if i % 2 == 0:
            answer += my_dict[0]
        else:
            answer += my_dict[1]
    return answer