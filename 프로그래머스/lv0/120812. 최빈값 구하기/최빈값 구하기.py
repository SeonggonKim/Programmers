def solution(array):
    num_list = list(set(array))
    num_count = []
    
    for num in num_list:
        num_count.append(array.count(num))
        
    if num_count.count(max(num_count)) > 1:
        answer = -1
    else:
        answer = num_list[num_count.index(max(num_count))]

    return answer