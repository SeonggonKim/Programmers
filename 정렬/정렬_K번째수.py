def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        _answer = array[commands[i][0]-1 : commands[i][1]]
        _answer.sort()
        answer.append(_answer[commands[i][2]-1])
    return answer