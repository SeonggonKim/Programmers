def solution(s):
    my_dict = {}
    my_list = []
    
    for i in range(len(s)):
        if s[i] not in my_dict:
            my_dict[s[i]] = -1
            my_list.append(my_dict[s[i]])
            my_dict[s[i]] = i
        else:
            my_dict[s[i]] = i - my_dict[s[i]]
            my_list.append(my_dict[s[i]])
            my_dict[s[i]] = i
            
    return my_list
