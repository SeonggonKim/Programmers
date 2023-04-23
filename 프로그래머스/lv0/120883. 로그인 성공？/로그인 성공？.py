def solution(id_pw, db):
    my_dict = {}
    for i in db:
        my_dict[i[0]] = i[1]
    
    if id_pw[0] not in my_dict:
        answer = "fail"
    elif id_pw[0] in my_dict and id_pw[1] == my_dict[id_pw[0]]:
        answer = "login"
    else:
        answer = "wrong pw"
    return answer