def solution(rsp):
    answer = ''
    my_dict = {'2':'0', '0':'5', '5':'2'}
    
    for i in rsp:
        answer += my_dict[i]
    return answer