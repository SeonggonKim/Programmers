def solution(age):
    
    answer = ''
    
    num = '0123456789'
    eng = 'abcdefghij'
    my_dict = {}
    for i in range(len(num)):
        my_dict[num[i]] = eng[i]
        
    for j in range(len(str(age))):
        answer += my_dict[str(age)[j]]
    return answer