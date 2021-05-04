def solution(name):
    answer = 0
    location = []
    for i in range(len(name)):
        if name[i] != 'A':
            location.append(i)
    if location == []:
        answer = 0
    elif location[0] <= len(name) / 2:
        answer += location[0]
    else:
        answer += (len(name) - location[0])

    for i in range(1, len(location)):
        if location[i] - location[i-1] > location[i-1] + (len(name) - location[-1]):
            answer += location[i-1] + (len(name) - location[-1])
        else:
            answer += location[i] - location[i-1]
    for i in range(len(name)):
        if ord(name[i]) > ord('N'):
            answer += ord('Z') +1 - ord(name[i])
        else:
            answer += ord(name[i]) - 65

    return print(location, answer)