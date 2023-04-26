def solution(emergency):
    answer = []
    my_list = sorted(emergency, reverse=True)
    my_dict = {}
    for i in range(len(my_list)):
        my_dict[my_list[i]] = i+1
    
    for j in emergency:
        answer.append(my_dict[j])
        
    return answer