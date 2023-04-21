def solution(numer1, denom1, numer2, denom2):
    answer = []
    answer.append(numer1 * denom2 + denom1 * numer2)
    answer.append(denom1 * denom2)
    
    both = []
    for i in range(1, max(answer)+1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            both.append(i)
    both_max = max(both)
    
    for j in range(len(answer)):
        print(answer)
        answer[j] /= both_max
        answer[j] = int(answer[j])
    print('answer:', answer)
        
    return answer