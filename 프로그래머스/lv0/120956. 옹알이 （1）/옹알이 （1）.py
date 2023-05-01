def solution(babbling):
    my_list = ['aya','ye','woo','ma']
    cnt = 0
    
    for bab in babbling:
        for word in my_list:
            if word in bab:
                bab = bab.replace(word, ' ')
            else:
                pass
        bab = bab.split()
        
        if len(bab) == 0:
            cnt += 1
        
    return cnt