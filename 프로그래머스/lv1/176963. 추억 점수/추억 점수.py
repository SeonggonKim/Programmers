def solution(name, yearning, photo):
    answer = []
    my_dict = {}
    for i in range(len(name)):
        my_dict[name[i]] = yearning[i]
    
    for j in photo:
        score = 0
        for k in j:
            if k in my_dict:
                score += my_dict[k]
        answer.append(score)
    return answer
